import sys





def loop(n):
    x = 1
    y = 2
    for a in range (0, n):
        z = x + y
        print(z)
        x = y
        y = z


def main():

    print("1aRa1")
    print("This programs seeks to print the fibonacci numbers.")
    n = int(input("Position of the sequence: \n >>>"))
    print("1")
    print("1")
    print("2")
    print(loop(n))

if __name__ == "__main__":
    main()
