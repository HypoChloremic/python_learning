'''
This is a test case of something stupid that Java does and does not work in Python
'''

class random:
	def method2(self, arg):
		print('the first constructor')

	def method2(self, mogabe, mogadisho):
		print('the second constructor')

	def method(self, *args, **kwargs):
		method2(*args, **kwargs)

if __name__ == '__main__':
	
	run = random()
	run.method2(10, 20, mogadisho)
	run.method2(arg=10)


		