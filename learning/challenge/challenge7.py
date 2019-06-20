# Arithmetic progression
# A + (A+B) + (A+2B) + (A+3B) + ... + (A+(C-1)B))

def main():
    N = int(input("data:\n"))
    l = []
    for x in range(0,N):
        a,b,c = input().split(" ")
        a,b,c = int(a),int(b),int(c)
        s = 0
        for each in range(0,c):
            s += a + (b*each)
        l.append(s)
    print("\nanswer:")
    for each in l:
        print(each, end=" ")
main()
