# rijeci 
 
def main(input):
	a = "a"
	for x in range(input):
		a = a.replace("b","by").replace("a","b").replace("y","a")
	print(a)
if __name__ == '__main__':
    main(4)