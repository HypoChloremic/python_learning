from concurrent.futures import ThreadPoolExecutor

import time

def func(x,y):
	print("Started func")
	time.sleep(5)
	return x+y


def run():

	# creates a pool of max_workers amount of threads. . .
	pool = ThreadPoolExecutor(max_workers=8)

	# we submit our function with the 
	# given parameters, i.e. x and y
	# and it starts running in the thread
	fut  = pool.submit(func, 2,5)

	# this is the callback function
	# it will be called once we get the result. 
	fut.add_done_callback(result_handler)


def result_handler(fut):
	# seems that when we create a add_done_callback
	# we are passing the futures object to the 
	# result_handler
	print("The callback function, i.e. the result_handler")

	# we therefore wait for the result here
	result = fut.result()
	print(f"Got: {result}")

run()
print("We are not blocking the caller anymore\n but are free to continue work")