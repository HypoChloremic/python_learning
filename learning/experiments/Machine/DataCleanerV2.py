import re

def main():
    def bagged():    
        fileName = input("Please enter the file name (enter the file-type as .fileType): ") 
        with open(fileName, "r") as file:
            data= file.read()
        x = re.findall(r'\d+,(.*?)\.0,Miscellaneous', data)
        data = data.replace("-","")
        y = re.findall(r'Bagged plant 1,400\.0,Yes,\d+,(.*?)\.0', data)
        with open("Cleaned."+fileName, "a") as file:
            a = 0
            for each in x:
                file.write(each + " " + y[a] + "\n")
                a+=1
    def iron():
        fileName = input("Please enter the file name (enter the file-type as .fileType): ") 
        with open(fileName, "r") as file:
            data= file.read()
        x = re.findall(r'\d+,(.*?)\.0,Mining', data)
        data = data.replace("-","")
        y = re.findall(r'Iron ore,6.0,No,\d+,(.*?)\.0', data)
        with open("Cleaned."+fileName, "a") as file:
            a = 0
            for each in x:
                file.write(each + " " + y[a] + "\n")
                a+=1
    iron()
        
if __name__=="__main__":
    main()
