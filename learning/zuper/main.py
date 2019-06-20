"""
The deal with super is that you can easily call 
a function of a parent or a sister class that you have inherited, without
necessarily calling the classes then their functions
an example
"""


class Parent:

	def __init__(self, i):
		print(i)

class Sister:
	def __init__(self):
		print("asda")

class Daughter(Parent, Sister):
	def __init__(self):
		super().__init__("asa")

""" What we note in the above case is that it is the parent class' __init__
function that is called and not the sister's. We assume that this can be attributed 
to the fact that the Parent was inherited first, and the Sister second. This
can be tested by exchanging the positions of the two classes when we inherit them
during the class declaration of Daughter. 
"""

if __name__ == '__main__':
	d = Daughter()