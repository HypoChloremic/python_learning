def main(inp):
	print(count(inp))

def count(inp):
	d = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
	
	if inp%10 == 0:
		print(inp)
	
	else:
		print(d.get((inp%10)))


if __name__ == '__main__':
	main(200)