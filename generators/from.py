# From the Dave Beazley tut, final frontiers

# seems like you can use from, 
# gives some strange behaviour

def comb(a,b):
	# seems like the from statement
	# consumes the iterables before moving
	# onto the next yield statement.
	yield from a
	yield from b

def run():
	a = [1,2,3,4]
	b = [5,6,7,8]
	combRun = comb(a,b)
	for i in combRun:
		print(i, end="  ")

run()