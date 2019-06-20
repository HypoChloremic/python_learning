import sys

def loop(w):
    x = 1
    y = 1

    if w == 1:
        return x
    elif w == 2:
        return y

    else:
        k = w-2
        for a in range (0, k):
            z = x + y
            x = y
            y = z
        return z


def main():

    print("1aRa1")
    print("This programs seeks to print the fibonacci numbers.")
    n = int(input("Position of the sequence: \n >>>"))
    print(loop(n))

if __name__ == "__main__":
    main()
