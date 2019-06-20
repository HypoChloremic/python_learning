class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self):
		
		self.w = [1,2,3]

	def o(self):
		o = self.w[:]
		o.append(2)
		o.append(3)
		print(self.w, o)
		self.p(o[:])
		print(self.w, o)

	def p(self, ar):
		ar.append(2)
		print(ar)

if __name__ == '__main__':
	o = []
	assert o[0]
	print(2)
		