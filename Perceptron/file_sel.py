import tkinter as tk
import csv
from tkinter import filedialog, messagebox

class file:

    def __init__(self):
        pass

    def get_file(self):
        root = tk.Tk()
        root.withdraw()  # Hide the root window
        file_path = filedialog.askopenfilename(title="Eliga el archivo CSV", filetypes=[("CSV files", "*.csv")])
#        print(f"Selected file: {file_path}")
        return self._read_info(file_path)

    def _read_info(self, path:str) -> dict:
        data=[]
        with open(path, newline='') as f:
            spamreader = list(csv.reader(f))
            spamreader.pop(0)
            n=len(spamreader[0])
            for i in range(n):
                data.append([float(x[i]) for x in spamreader]) #lista compuesta de las listas de los inputs, última lista es valor esperado

        return data


if __name__=="__main__":
    file().get_file()