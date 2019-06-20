from multiprocessing import Process, Pool
from time import sleep


def hello(a="Hello"):
	while True:
		print(a)
		sleep(1)

def world(b="world"):
	print(b)

if __name__ == '__main__':
	a = (world(b="hej"), world(b="på"), world(b="dig"))
	for each in a:
		Process(target=each).start()