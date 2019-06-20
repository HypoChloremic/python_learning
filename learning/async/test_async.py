# Testing out some stuff with async and await


async def hello(name):
	print ("hello" + name)
	return "hello" + name

# We can use the await statement in coroutines to call
# coroutines as normal functions; i.e. what it implies is that 
# if we runt return await func(*args) in a courtoune
# is like running return func2(*args) in a normal def function

async def await_hello(func, *args):
	return await func(*args)

def run(coro, *args):
	try:
		# We need to create the coroutine object before we start using it. 
		# 
		g = coro(*args)
		# In order to run the coroutine from a normal function, we need to
		# send it a value, in this case None.
		g.send(None)

	# However, the coroutine will run til it returns a StopIteration
	# which we need to catch, and then catch the value of that 
	# exception, so as to find out what it has produced
	except StopIteration as e:
		return e.value

print(run(await_hello, hello, "wut"))