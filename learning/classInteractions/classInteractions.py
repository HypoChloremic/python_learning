

class firstClass:
	def __init__(self):
		self.var1 = 1

class secondClass:
	def __init__(self, classObject):
		print(classObject.var1)
		classObject.var1 = 3

if __name__ == '__main__':
	i = firstClass()
	i.var1 = 2
	o = secondClass(i)
	# this implies that a passed class
	# to another class is simply a pointer
	# i.e. we can change the original class
	# despite it being passed
	print(i.var1)
