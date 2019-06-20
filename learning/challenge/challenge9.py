# Linear regression
# y = mx + b

import matplotlib.pyplot as plt
import numpy as np

def main():
    a,b = input("data:\n").split(" ")
    a,b = int(a),int(b)
    lx,ly = [],[]
    for x in range(a,b+1):
        x,y = input("%s: " %x).split(" ")
        x,y = float(x),float(y)
        lx.append(x), ly.append(y) 
    print(lx)
    plt.scatter(lx,ly)
    par = np.polyfit(lx, ly, 1, full=True)
    coeffs = np.polyfit(lx,ly, 1)
    fittedx = np.linspace(min(lx), max(lx), 200)
    fittedy = np.polyval(coeffs, fittedx)
    plt.plot(fittedx, fittedy)
    plt.show()
    print(coeffs)
main()
