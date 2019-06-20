# async with statement
# (c) Ali Rassolie

class AClass():
	"""We use the async statement for the definitions
	of the enter and the exit special funcitons. However, 
	it is important to note that these are called aenter and 
	aexit, and not enter and exit, maybe to distinguish them
	from the normal ones, for the normal functions"""
	async def __aenter__(self):
		print("Entering")

	async def __aexit__(self, _, __, ___):
		print("Exiting")


def run(coro):
	try:
		coro_func = coro()
		coro_func.send(None)
	except StopIteration as e:
		a = e.value
		print(a)

@run
async def main():
	"""Here we first instatiate the class 
	and call it a, before we go on and use the 
	with statement to use the enter and the exit functions
	we defined earlier"""
	a = AClass()
	
	async with a:
		print("inside main")

