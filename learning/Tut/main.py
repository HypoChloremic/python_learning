import sys
import re
import time

def cleaner(fileName):
    fileName = fileName +".txt"
    file = open(fileName, "r")
    fileData = str(file.read())
    file.close()

    fileName = "x" + fileName 
    a = open(fileName, "w")
    x = fileData.replace(".", "")
    y = x.replace(",", "")
    z = y.replace(":", "")
    c = z.replace("(", "")
    d = c.replace(")", "")
    a.write(d)
    a.close()

def main():
    print("Text Analyzer V1")
    fileName = input("Please input the name of the txt file:\n>")
    cleaner(fileName)
    fileName = "x" + fileName + ".txt"
    file = open(fileName, "r")
    k = str(file.read())
    k = k.split()
    k.sort()
    #print(k)

    z = int(0)
    x = int(0)
    w = int(0)
    for each in k:
        if x != k[z]:
            print(k.count(k[z]), k[z])
            x = k[z]
            z+=1
            w+= 1
            
        elif x == k[z]:
            z+=1
            
        else:
            return "Error 01"

    print("Number of unique words: " + str(w) + "\nTotal number of words: " + str(len(k)))
    print("Total number of words to unique words ratio: "+ str(len(k)/w))
    EXIT()

def EXIT():
    input("Press return to exit.")
    time.wait(10)

if __name__=="__main__":
    main()
