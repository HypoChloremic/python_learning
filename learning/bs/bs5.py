import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import matplotlib.animation 


class Grid:
	
	def __init__(self, x, y):
		print(self.na(x,y))
            
	def na(self, x, y):
		self.list1 = [x for x in range(0, self.x)]
		self.list2 = [y for y in range(0, self.y)]
		ar = np.array([self.list1, self.list2])
		return ar

def main():
	pass


        
if __name__ == '__main__':
	a = Grid()
