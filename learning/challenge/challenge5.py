def main():
    k = input("data:\n").split(" ")
    k = [int(x) for x in k]
    k.sort()
    print("answer:\n%s %s" %(str(k[-1]),str(k[0])))
main()
    
