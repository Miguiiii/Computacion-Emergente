import file_sel as fs
import matplotlib.pyplot as plt

class graph():

    def __init__(self):
        self.data=fs.file().get_file()
        plt.scatter(self.data[0], self.data[1], c=self.data[len(self.data)-1])
        plt.show()


if __name__=="__main__":
    graph()