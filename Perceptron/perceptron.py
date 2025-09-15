import math as m


class adeline:
    def __init__(self, data:list):
            self.update_w=lambda w, t, e, p: w+t*e*p
            self.update_b=lambda b, t, e: b+t*e
            self.act_esc = lambda x: 1 if x>0 else 0
            self.act_bisig = lambda x: (1-m.exp(-x))/(1+m.exp(-x))
            self.act_sig = lambda x: 1/(1+m.exp(-x))
            self.model=data
            self.nw:int=len(self.model)-1 #el numero de pesos
            self.pesos=[]
            print(f"El Adeline tendrá {self.nw} inputs y 1 neurona")
            for i in self.nw:
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
                s=input("Ingrese un valor entero para la cantidad máxima de iteraciones (100 por defecto, presione Enter): ")
                if t=="":
                    self.iter=100
                    break
                try:
                    self.iter=float(t)
                    break
                except:
                    print("Valor no aceptado, intente de nuevo")

            while True:
                a=input("Eliga la funcion de activación a utilizar:\n1 .- Escalonada (Ouptut es 1 o 0)\n2 .- Sigmoide (Output de 0 a 1)\n 3 .- Sigmoide bipolar (Output de -1 a 1)")
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

    def train(self):
        pass