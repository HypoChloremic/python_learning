def gen():
	print("first part, before item")

	# seems like, if we do not generator.send()
	# anything, then the outcome will be that we
	# will declare item = None.
	item = yield

	print("before value")
	yield item

g = gen()


next(g)
# what we see is that the generator.send()
# will also advance the generator to the 
# next yield statement. 
# if we do not send anything, but use next()
# instead, then we will be sending None. 
val = g.send("hello")

print(val)