import sys

def loop (x):
    for k in range(x):
        print(k+1)
    y = print ("End")
    return y






def main ():
    x = int(input("Please input a value for x: /n >"))
    print(loop(x))





if __name__=="__main__":
    main()
