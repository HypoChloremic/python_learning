def main():
    N = int(input("data:\n"))
    v = ["a","e","y","u","o","i"]
    l = []
    q = 0
    for x in range(0,N):
        z = input()
        z.lower().replace("\n", "")
        print(z)
        for w in v:
            a = z.count(w)
            q += a
        l.append(q)
        q=0
    print("\nanswer:")
    for x in l:
        print(x, end=" ")
main()
