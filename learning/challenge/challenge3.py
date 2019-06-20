def main():
    N = int(input("input data: \n"))
    l = []
    for x in range(0,N):
        a,b = input().split()
        if int(a) > int(b):
            l.append(int(b))
        else:
            l.append(int(a))
    print("answer:\n")
    for x in iter(l):
        print(x, end=" ")



main()
