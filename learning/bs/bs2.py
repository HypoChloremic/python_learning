def main():
	with open("number.txt", "r") as file:
		data = file.read()
		data = data.split("\n")
	x = [row.split("\t") for row in data[:5]]
	print(function(x))

def function(x):
    sum=0
    for el in x[0:]:
        sum += int(el[0])
    return sum

if __name__=="__main__":
	main();
    
