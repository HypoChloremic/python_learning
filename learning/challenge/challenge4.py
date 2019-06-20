def main():
    N = int(input("data: \n"))
    l = []
    for x in range(0,N):
        k = input().split(" ")
        k = [int(x) for x in k]
        k.sort()
        l.append(k[0])

    print("\nanswer:")
    for x in iter(l):
        print(x, end=" ")

main()
