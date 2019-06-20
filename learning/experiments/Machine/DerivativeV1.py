import matplotlib.pyplot as plt
import numpy as np

def main():
    dataName = input("Please input the name of the data-file (.txt): ")+".txt"
    with open(dataName, "r") as file:
        data = file.read()

    x = [row.split(" ") for row in data[:179]]
    y = [row.split(" ") for row in data[:179]]
    print(x)
    x = np.array(x)
    y = np.array(y)
    print(x)
    x = x.astype(np.float)
    y = y.astype(np.float)
    x2 = np.linspace(x.min(),x.max(), 500)
    y2 = np.spline(x,y,x2)
    derivative(x,y)
    
def derivative(x,y):
    pass

if __name__=="__main__":
    main()
