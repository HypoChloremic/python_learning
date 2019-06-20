import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline, UnivariateSpline

def main():
    dataFile = input("Please input the name of the data file (.txt): ") + ".txt"
    with open(dataFile, "r") as file:
        data=file.read()

        
    answer = input("Is this 179 Y/N? ")

    if answer =="Y" or answer =="y":
        data = data.split("\n")
        x = [row.split(" ")[0] for row in data[:180]]
        y = [row.split(" ")[1] for row in data[:180]]
        x = np.array(x, dtype=np.float)
        y = np.array(y, dtype=np.float)
            
        x2 = np.linspace(x.min(),x.max(), 50000)
        sp1 = UnivariateSpline(x,y)
        y2 = sp1(x2)

        j = plt.figure(1)
        plt.plot(x,y)
        plt.plot(x2,y2)
        plt.show(1)
        derivative(x2,y2)
    
    else:
        data = data.split("\n")
        x = [row.split(" ")[0] for row in data[:1300]]
        y = [row.split(" ")[1] for row in data[:1300]]
        x = np.array(x, dtype=np.float) # The float part can be expressed separately by x = x.astype(np.float) where astype(dtype=...)
        y = np.array(y, dtype=np.float)

    
        sp1 = UnivariateSpline(x,y)
        x2 = np.linspace(x.min(), x.max(), 5000)
        y2 = sp1(x2)
        j = plt.figure()
        plt.plot(x2, sp1(x2), "g", lw=3)
        plt.plot(x,y)
        plt.show(1)
        print(sp1(x2))
        derivative(x2, y2)
        
        
        
                

def derivative(x2,y2):
    
    
    
if __name__ =="__main__":
    main()
