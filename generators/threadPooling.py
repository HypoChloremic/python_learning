from concurrent.futures import ThreadPoolExecutor

import time

def func(x,y):
	print("Started func")
	time.sleep(1)
	return x+y

# creates a pool of max_workers amount of threads. . .
pool = ThreadPoolExecutor(max_workers=8)

# we submit our function with the 
# given parameters, i.e. x and y
fut  = pool.submit(func, 2,5)

# the function is running now, once it finishes
# it'll pass the result to r

# however what happesn here is that we are blocking 
# the caller, i.e. the caller of functions
# what we can do is to register a callback function
# whereby once we get a result, it will produce it and
# return it to us
r = fut.result()

print(f"Got: {r}")
