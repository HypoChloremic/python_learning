from multiprocessing import Process
from multiprocessing import Queue
from random import random
from time import sleep

def hej(q):
	print("sdfsdf")
	for i in range(3):
		sleep(1)
		print(f"{i}")
	d = [i for i in range(5000)]

	return q.put(["wut",d])

if __name__ == '__main__':
	q = Queue()
	jobs = list()

	for i in range(2):
		p = Process(target=hej, args=(q,))
		jobs.append(p)
		p.start()

	print("outside")
	
	while not q.empty():
		print("q aint empty")
		print(q.get())

		
	for p in jobs:
		p.join()


	