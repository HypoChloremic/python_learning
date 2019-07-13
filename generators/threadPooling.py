from concurrent.futures import ThreadPoolExecutor

import time

def func(x,y):
	print("Started func")
	time.sleep(5)
	return x+y

# creates a pool of max_workers amount of threads. . .
pool = ThreadPoolExecutor(max_workers=8)

# we submit our function with the 
# given parameters, i.e. x and y
fut  = pool.submit(func, 2,5)

# the function is running now, once it finishes
# it'll pass the result to r
r = fut.result()

print(f"Got: {r}")
