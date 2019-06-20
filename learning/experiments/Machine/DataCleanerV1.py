import re

def DataCleaner():
try: 
    fileName = input("Please input the name of the Lobster-file (.txt): ")+".txt"
    with open(fileName, "r") as file:
        data = str(file.read())
    x = re.findall(r'\d,(\w.*?),Food and Drink', data)
    y = re.findall(r'No,\d,(\w.*?)\.', data)
except:
    fileName = input("Please input the name of the file: ")
    with open(fileName, "r") as file:
        data = file.read()
    x = re.findall(r'\d{10}', data)
    y = re.findall(r'\d{1-4}', data)
    
cleanedName= input("Please enter the Cleaned File Name (Look in working directory for the file): ")
with open(cleanedName, "a") as file:
    for each in range(0, len(y)):
        try:
            file.write(x[each] + " ")
            file.write(y[each] + "\n")
        except:
            continue
with open(cleanedName, "r") as file:
    data = file.read().split("\n")
    data.pop()
    del data[0]
    data.sort()

with open("2"+cleanedName, "a") as file:
    for each in range(0, len(data)):
        try:
            file.write(data[each] + "\n")
        except:
            pass

DataCleaner()
