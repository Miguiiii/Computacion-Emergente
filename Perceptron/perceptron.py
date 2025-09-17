import math as m
import file_sel as f
from grapher import Graph

class Adeline:
    def __init__(self):
        self.act_esc = lambda x: 1 if x>0 else 0
        self.act_bisig = lambda x: (1-m.exp(-x))/(1+m.exp(-x))
        self.act_hiper = lambda x: (m.exp(2*x)-1)/(m.exp(2*x)+1)
        self.act_sig = lambda x: 1/(1+m.exp(-x))
        self.pesos=[]
        self.pred = []
        self.err = []
        self.mse=0
        self._ask_model_data()
        self.preddict()
        self.get_errors()
        self.mostrar_res()
        self.show_graphs()
        while True:
            ans=input("Desea entrenar el modelo? (y/n)")
            if ans.lower()=="n":
                break
            elif ans.lower()=="y":
                self.train()
                print("Despues de ser entrenado, el modelo resultante fue:")
                self.mostrar_res()
                self.show_graphs()

    def mostrar_res(self):
        print(f"Pesos: {self.pesos}")
        print(f"Bias {self.bias}")
        print(f"Predicciones: {self.pred}")
        print(f"Errores: {self.err}")
        print(f"Media de los errores cuadrado (MSE): {self.mse}")

    def _ask_model_data(self):
        self.model=f.File().get_file()
        self.expect=self.model.pop()
        self.nw:int=len(self.model) #el numero de pesos
        print(f"El Adeline tendrá {self.nw} inputs y 1 neurona")
        for i in range(self.nw):
            while True:
                try:
                    self.pesos.append(float(input(f"Ingrese un valor para el peso w{i+1}: ")))
                    break
                except:
                    print("Valor no aceptado, intente de nuevo")

        while True:
            b=input("Ingrese un valor para el bias (0 por defecto, presione Enter): ")
            if b=="":
                self.bias=0
                break
            try:
                self.bias=float(b)
                break
            except:
                print("Valor no aceptado, intente de nuevo")

        while True:
            a=input("Eliga la funcion de activación a utilizar:\n1 .- Escalonada (Ouptut es 1 o 0)\n2 .- Sigmoide (Output de 0 a 1)\n3 .- Sigmoide bipolar (Output de -1 a 1)\nIngrese la selección: ")
            try:
                a=int(a)
                if a not in (1, 2 , 3):
                    raise Exception
                break
            except:
                print("Valor no aceptado, intente de nuevo")
        if a==1:
            self.activate=self.act_esc
        if a==2:
            self.activate=self.act_sig
        if a==3:
            self.activate=self.act_bisig

    def pre_training(self):
        while True:
            t=input("Ingrese un valor entre 0 y 1 para la tasa de aprendizaje (1 por defecto, presione Enter): ")
            if t=="":
                self.tasa=1
                break
            try:
                self.tasa=float(t)
                break
            except:
                print("Valor no aceptado, intente de nuevo")

        while True:
            e=input("Ingrese un valor entero para la cantidad máxima de iteraciones (100 por defecto, presione Enter): ")
            if e=="":
                self.epoch=100
                break
            try:
                self.epoch=float(e)
                break
            except:
                print("Valor no aceptado, intente de nuevo")
        while True:
            e=input("Ingrese un valor para el error mínimo objetivo (0.5 por defecto, presione Enter): ")
            if e=="":
                self.obj_err=0.5
                break
            try:
                self.obj_err=float(e)
                break
            except:
                print("Valor no aceptado, intente de nuevo")

    def preddict(self):
        for i in range(len(self.model[0])): #realiza las predicciones con los pesos y el bias actuales
            yt=sum([self.model[j][i]*self.pesos[j] for j in range(len(self.pesos))])+self.bias
            yt=self.activate(yt)
            self.pred.append(yt)

    def get_errors(self):
        self.err = [self.expect[i]-self.pred[i] for i in range(len(self.pred))]
        self.mse=sum(list(map(lambda x: x*x, self.err)))/len(self.err)
    
    def train(self):
        self.pre_training()
        for whatever in range(self.epoch):
            self.pred=[]
            self.preddict()
            #revisar si el error es suficientemente bajo antes de realizar correciones
            self.get_errors()
            if self.mse < self.obj_err:
                break

            for i in range(len(self.err)): #update los pesos y el bias
                self.pesos=list(map(lambda w, x: w+self.tasa*self.err[i]*x[i],self.pesos, self.model[:-1]))
                self.bias+=self.tasa*sum(self.err)
        
    def show_graphs(self):
        cmap1 = [str(m.fabs(1-self.activate(x))) for x in self.expect]
        cmap2 = [str(m.fabs(1-x)) for x in self.pred]
        cmap3 = [(1.0, 0.0, 0.0) if m.fabs(x)>=1 else (m.fabs(x), 1.0-m.fabs(x), 0.0) for x in self.err]
        g=Graph(self.model[0], self.model[1], cmap1, cmap2, cmap3)
        g.mostrar()

if __name__=="__main__":
    a = Adeline()