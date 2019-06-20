import sys
import math



def loop(dx, n, a):

    A = 0
    #for x in range (aLim, bLim)
    for x in range (n):
        a2 = x*dx
        fnctValue = a*a2
        area = fnctValue * dx
        A = A+area
        print (A)
    return A    

def main():
    a    = float(input("Enter leading coefficient for linear function (ax): "))
    aLim = int(input("Enter left limit a: "))
    bLim = int(input("Enter right limit b: "))
    dx   = float(input("Enter delta x: "))
    n    = int((bLim - aLim)//dx)
    print (n)

    print(loop(dx, n, a))


if __name__=="__main__":
    main()
