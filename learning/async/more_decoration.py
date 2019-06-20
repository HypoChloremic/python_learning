# More decoration
# (c) Ali Rassolie

import asyncio

async def hello():
	asyncio.wait(1)
	print("Hello")

async def world():
	print("World")

def run(coro):
	try:
		coro().send(None)
	except StopIteration as e:
		return_value = e.value
		return return_value

@run
async def double():
	await hello()
	await world()