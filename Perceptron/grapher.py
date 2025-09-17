import file_sel as fs
import matplotlib.pyplot as plt
import math as m

class Graph():

    def __init__(self, x:list, y:list, cmap1, cmap2, cmap3):
        fig, (esper, pred, errs)=plt.subplots(1,3,figsize=(20,5))
        esper.scatter(x, y, c=cmap1, edgecolors="k")
        esper.set_title("Valores Esperados")
        esper.set_xlabel("X1")
        esper.set_ylabel("X2")
        pred.scatter(x, y, c=cmap2, edgecolors="k")
        pred.set_title("Valores Predecidos")
        pred.set_xlabel("X1")
        pred.set_ylabel("X2")
        errs.scatter(x, y, c=cmap3, edgecolors="k")
        errs.set_title("Errores en predicción (Verde=Correcto, Rojo=Incorrecto)")
        errs.set_xlabel("X1")
        errs.set_ylabel("X2")

    def mostrar(self):
        plt.show()


if __name__=="__main__":
    Graph()