def generator():
	# . . .

	yield

	# . . .
	result = None

	return result

g = generator()

next(gen)  			  # advance to next yield
g.send(item) 		  # send an item, (and seemingly advance to next yield)
g.close() 			  # terminate the generator
g.throw(exc, val, tb) # raise exception
result = yield from g # to delegate
