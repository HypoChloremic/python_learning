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
	a = [1,2,3,4, "a,"]
	b = [5,6,7,8, "b,"]

	for i in comb(a,b):
		print(i, end="  ")


def run2(): 
	a = [1,2,3,4, "a,"]
	b = [5,6,7,8, "b,"]
# based on the results, it seems that 
# itll consume everything in order, 
# however nested it looks. 
	for i in comb(comb(a,b), comb(b,b)):
		print(i, end="  ")
run2()