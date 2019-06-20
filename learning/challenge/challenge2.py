import numpy as np

def main():
    N = int(input("input value:\n"))
    l=[]
    for x in range(0,N):
       k = input().split()
       k = map(int, k)
       l.append(sum(k))
    print("answer:\n")
    for x in iter(l):
        print(x, end=" ")
main()
