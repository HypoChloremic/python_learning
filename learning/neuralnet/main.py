# Introduction to neural networks, incorporating sensible mathematics
# in accordance to deepideas.net
import numpy as np

class Operation:
	""" So an operation is the node where 
	you have a function that you wish to perform. 
	"""
	def __init__(self, input_nodes=[]):
		self.input_nodes = input_nodes
		self.consumers = []

		for input_node in input_nodes:
			# It seems that the input nodes will have the consumers
			# method in them, implying that they themselves are graphs?
			input_node.consumers.append(self)

		_default_graph.operations.append(self)

	def compute(self): 
		""" constructing operation
		"""
		pass

class add(Operation):
	def __init__(self, x,y):
		super().__init__([x,y]) # So these will be the input nodes. 

	def compute(self, x_value, y_value):
		self.inputs = [x_value, y_value]
		return x_value + y_value


class matmul(Operation):
	def __init__(self, a,b):
		super().__init__([a,b])

	def compute(self, a_value, b_value):
		self.inputs = [a_value, b_value]
		return a_value.dot(b_value)

class placeholder:
	def __init__(self):
		# We do not know what the consumer of this
		# object is at the moment, hence the improance to
		# initialize it.
		self.consumers=[]
		_default_graph.placeholders.append(self)

class Variable:
	def __init__(self, initial_value=None):
		self.value = initial_value
		self.consumers = []
		_default_graph.variables.append(self)

class Graph:
	# So this is essential for the entire system to function correctly
	# We notice that the graph, which I assume will contain the entire
	# system, and not just a node, has lists for each of the shits that
	# wanna perform, i.e. operations, placeholders, and variables. 
	def __init__(self):
	# Note that these are 
		self.operations   = []
		""" The placeholder has been raising eyebrows, cuz
		we did not get their exact purpose. What we notice however
		is that we may be having graphs that are not entirely defined
		initially, and that we wanna change parameters eventually, and 
		it is the placeholder's purpose. 
		"""
		self.placeholders = []
		self.variables    = []

	def as_default(self):
	# Note that this global shit will be used by the other classes
		global _default_graph
		_default_graph = self # Ive never seen anybody do it this way, but it seems
		 					  # to make the variables in the __init__ globally available
		 					  # which is very interesting indeed. 



class Session: 
	def run(self, operation, feed_dict={}):
		nodes_postorder = traverse_postorder(operation)
		for node in nodes_postorder:
			if type(node) == placeholder:
				node.output = feed_dict[node]
			elif type(node) == Variable:
				node.output = node.value
			else:
				node.inputs=[input_node for input_node in node.input_nodes]
				node.output = node.compute(*node.inputs)

			if type(node.output) == list:
				node.output = np.array(node.output)

		return operation.output

def traverse_postorder(operation):
    """Performs a post-order traversal, returning a list of nodes
    in the order in which they have to be computed
    
    Args:
       operation: The operation to start traversal at
    """

    nodes_postorder = []
    def recurse(node):
        if isinstance(node, Operation):
            for input_node in node.input_nodes:
                recurse(input_node)
        nodes_postorder.append(node)

    recurse(operation)
    return nodes_postorder

if __name__ == '__main__':
	Graph().as_default() # This creates a new graph
	A = Variable(np.array([[1,0], [0,-1]])) # that is contained 
											# in a Variable node
	b = Variable(np.array([1,1])) # Another value that we contain
								  # in a variable node
	x = placeholder() # This is a placeholder because we are going 
					  # supply its value eventually.
	y = matmul(A, x) # We would like to perform multiplication
	 				 # with the output of both of these nodes
	z = add(y,b)	 # we are then adding each of their values. 

	session = Session()
	output = session.run(z, {x:[1,2]})
	print(output)