import numpy as np
def main():
    print("Input Data:")
    l = input()
    l = l.split(" ")
    l = np.array(l, int)
    print("\nanswer:\n%s"%sum(l))

main()
