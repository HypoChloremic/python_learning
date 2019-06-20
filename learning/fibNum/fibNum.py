# Comparing performande between this and c++
# (c) 2017 Ali Rassolie



def fib(num):
	a,a2 = 0,1

	for x in range(num):
		temp = a2
		a2 = a2 + a
		a = temp
	return a2

def fib_slow(n):

	if n == 0: return 0
	elif n == 1: return 1
	else: return fib_slow(n-1)+fib_slow(n-2)

if __name__ == '__main__':
	print(fib_slow(34))