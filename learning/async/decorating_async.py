# We are to use decorators to run this shit!
# (c) Ali Rassolie

def run(coro):
	"""In order to call an async func
	from the inside of a normal func def, we need
	a try statement. Firstly, we instantiate the coro, and then
	send it None, in order to run it. This will raise a StopIteration
	error which we catch, in addition to catching and 
	returning the e.value as well"""

	try:
		coro_func = coro()
		coro_func.send(None)
	
	except StopIteration as e:
		a = e.value
		print(a)

@run
async def hello():
	print("We are inside the coro")
	return "Hello"