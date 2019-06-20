# For producing random numbers
# (cc) Ali Rassolie 2017

import numpy as np
import random

class randomNum:
	def __init__(self):
	# We are producing randomg values around a given line, 
	# for use in regression
		print("[randomNum] Initializing")

	def ranLinVal(self, m=1, b=0, offset=4, ceil=10000):
		print("[ranLinVal] Producing values")
		dataset = [[i, self.ranLin(x=i, m=m, b=b, offset=offset)] for i in range(ceil)]
		self.x_val = [i for i,k in dataset]
		self.y_val = [k for i,k in dataset]

		return dataset
	
	def ranLin(self, x, m, b, offset):
		curr_y = (m*x) + b
		Offset = (random.random() * offset)
		if random.choice([True, False]):
			Offset = (-Offset)
		else:
			pass
		return curr_y + Offset

	def get_x_y(self):
		"""This methods kwargs will be passed to ranLinVal
		i.e. we are using ranLinVal's kwargs"""
		return self.x_val,self.y_val

if __name__ == '__main__':
	process = randomNum()
	x,y = process.get_x_y()
	print(x,y)