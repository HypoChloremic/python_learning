import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import UnivariateSpline
import urllib.request as ur
import time
# Version 4 of the derivative grapher.
# This version is utilizing classes in order to generalize the structure, and remove
# the necessity for repetetive coding.
# Sharpening may be required for later versions. 
class Graph:
    def __init__(self, dataFile, w = 0, z = 180):
        print("Hello")
        with open(dataFile) as file:
            data = file.read()
            data = data.split("\n")
        self.x = [row.split(" ")[0] for row in data[w:z]]
        self.y = [row.split(" ")[1] for row in data[w:z]]            
        self.x = np.array(self.x, dtype=np.float)
        self.y = np.array(self.y, dtype=np.float)
        self.x2= np.linspace(self.x.min(), self.x.max(), 9000)
        sp1 = UnivariateSpline(self.x,self.y)
        self.y2 = sp1(self.x2)
        Graph.graph(self, "a", self.x2, self.y2)
        Graph.derivative(self)

    def derivative(self):
        self.y3 = []
        h = 2*(self.x2[1]-self.x[0])
        a = len(self.x2)-1
        a2 = len(self.x2)
        self.x3 = self.x2[:a]
        for each in range(0, a):
            k = (self.y2[each+1]-self.y2[each])/h
            self.y3.append(k)
        self.y3 = np.array(self.y3, dtype=np.float)
        self.x3 = np.array(self.x3, dtype=np.float)
        Graph.graph(self, "a2", self.x3, self.y3)

    def graph(self, variable, xValue, yValue): # This removes the necessity to repetetively specify the graph part. 
        v2 = variable + str(1)
        self.v2 = plt.figure()
        self.variable = self.v2.add_subplot(111)
        self.variable.plot(xValue, yValue)

    def average(self):
        avgSum = 0
        for each in self.y2:
            avgSum += each
        average = avgSum / len(self.y2)
        print("Average: %s" % average)

class Miner(Graph): # Inherits the methods of Graph, in order to simply use the file created by the miner
                    # This perhaps represents the complete version of the graphing aspect of the program.
                    # Further data mining may be necessary. For instance: a function which identifies the gradient
                    # of specific slopes, where a specific incline will generate a higher probability for further increase and the like.
                    
    def __init__(self):
        itemName = input("What is the name of the item?: ")
        itemId   = input("What is the item id? ")
        url = "http://services.runescape.com/m=itemdb_rs/api/graph/"+itemId+".json"
        data = str(ur.urlopen(url).read())
        data = data.replace("daily","").replace("average","").replace("b'", "").replace("{:","").replace("{","").replace("}","").replace("'","").replace('"','').replace(",", "\n").replace("0:",",").replace(":","").replace(","," ")
        date = str(time.strftime("%d%m%y"))
        txtFile1=itemName+date+".txt"

        with open(txtFile1, "w") as file:
            file.write(data)
        Graph.__init__(self, txtFile1)
        Graph.average(self)

if __name__ == "__main__":
    Allo = Miner()
