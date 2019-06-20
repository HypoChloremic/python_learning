# Let's see if we can do some asynchronous stuff with this shit

import asyncio


async def hello():
	a = 0
	asyncio.time(10)
	
	return "hello"

async def world():
	return "world"

async def combine():
	await hello()
	await world()

def run(func1, *args):
	try:
		g = func1(*args)
		g.send(None)
	
	except StopIteration as e:
		return e.value

run(combine)