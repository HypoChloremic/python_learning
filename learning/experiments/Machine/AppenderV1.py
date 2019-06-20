
def main():
    file1 = input("Please enter the name of the bigger file: ") + ".txt"
    file2 = input("Please enter the name of the smaller file: ") + ".txt"     

    with open(file1, "a") as file1:
        with open(file2, "r") as file:
            data = str(file.read())
            file1.write("\n" + data)
    

if __name__=="__main__":
    main()
