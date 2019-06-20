import sys, math, matplotlib.pyplot as plt, numpy as np

def main():
    dataFile=input("please input the name of the data file (.txt is not necessary): ")+".txt"
    with open(dataFile, "r") as file:
        data = file.read()
    data = data.split("\n")
    x = [row.split(" ")[0] for row in data[:181]]
    y = [row.split(" ")[1] for row in data[:181]]
    print(x)
    x2= [row.split(" ")[0] for row in data[181:]]
    y2= [row.split(" ")[1] for row in data[181:]]
    print(y2)   
    x,y,x2,y2=np.array(x),np.array(y),np.array(x2),np.array(y2)
    plt.figure().add_subplot(111).plot(x,y).plot(x2,y2)
    plt.figure().add_subplot(111).plot(x2,y2)
    plt.show()
    
    



if __name__=="__main__":
    main()
