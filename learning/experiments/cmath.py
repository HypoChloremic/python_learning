import cmath

def main():
	a = 10 + 5j
	print(cmath.phase(a), abs(a), cmath.rect(a))


if __name__ == '__main__':
	main()