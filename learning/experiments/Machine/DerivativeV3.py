import scipy.interpolate as sci
import matplotlib.pyplot as plt
import numpy as np



def data_graph(dataFile, w, z):
    #dataFile = input("Please input the name of the data file (.txt): ") + ".txt"
    with open(dataFile, "r") as file:
        data=file.read()
    data = data.split("\n")
    x = [row.split(" ")[0] for row in data[w:z]]
    y = [row.split(" ")[1] for row in data[w:z]]
    x = np.array(x, dtype=np.float)
    y = np.array(y, dtype=np.float)
        
    x2 = np.linspace(x.min(),x.max(), 9000000)
    sp1 = sci.UnivariateSpline(x,y)
    y2 = sp1(x2)
    
    j1 = plt.figure()
    j = j1.add_subplot(111)
    j.plot(x,y, label = "Raw Entry")
    j.plot(x2,y2, label = "Smoothed Entry")
    data_derivativeone(x2,y2)
    #data_derivativetwo(x2,y2)
def data_derivativeone(x2,y2):
    # Numerical Differentiation.
    # Primary issue here is to assign the x-value for the derivative.
    # One may utilize the (F(x+h)-F(x))\h where h would approach zero.
    # Approaching zero in turn can be done with the UnivariateSpline and linspace;
    # Values approaching zero there would imply that h would approach zero.
    # The definition of the derivative states the following: F´(x) = (F(x+h)-F(x))\h
    # which clearly implies that the derivative would be merely assigned to the specific x value.
    # 9*e+6 will be enough to bring it down to 1,7.
    y3 = []
    h = (x2[1]-x2[0])
    a = len(x2)-1
    x3= x2[:a]
    for each in range(0, a):
        k = (y2[each+1]-y2[each])/h
        y3.append(k)
    y3 = np.array(y3, dtype=np.float)
    x3 = np.array(x3, dtype=np.float)
    
    a1 = plt.figure()
    a = a1.add_subplot(111)
    a.plot(x3,y3, label = "One-point Derivative")

def data_derivativetwo(x2, y2):
    # This uses the following function: F´(x) = (F(x+h)-F(x-h))\2h
    y3 = []
    h = 2*(x2[1]-x2[0])
    a = len(x2)-1
    a2 = len(x2)-2
    x3= x2[:a]
    for each in range(1, a):
        k = (y2[each+1]-y2[each-1])/h
        y3.append(k)
        
    y3 = np.array(y3, dtype=np.float)
    x3 = x3[:a2]
    x3 = np.array(x3, dtype=np.float)
    
    a1 = plt.figure()
    a = a1.add_subplot(111)
    a.plot(x3,y3, label = "Two-point derivative")


if __name__ == "__main__":
    # Run tests here!



    
