# Async iteration
# (c) Ali Rassolie
# Tested in python 3.6

def run(coro):
	try:
		coro_func = coro()
		coro_func.send(None)
	except StopIteration as e:
		a = e.value
		print(a)

# The following only works in python 3.6 and beyond
async def call_it():
	yield "1"
	yield "2"

@run
async def it():
	async for x in call_it():
		print(x)
