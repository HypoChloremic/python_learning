import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Say we would like to create a simple network
# with one input node, one hidden layer
# and one output node. We would like, for the 
# activation function use a sigmoid (then moving
# on to relu and softmax).
# 
# the inputnode, in essence it is static, and 
# it will not change by tensorflow, instead it is
# changed externally
inputNodeValue = tf.placeholder(tf.float32, [1,1])

# Aight, we would now like to initialize the 
# weights. Initialization can be done using the 
# tf.zeros method, where these are generated in 
# accord to the provided shape. I.e. by inputting
# a specific shape, we output a zeroed matrix, with
# with the given dimensions. In turn, this implies 
# that we are able to produce the weight matrix we 
# were initially interested in. 
#
# Based upon some ez maths, we determine that the shape
# should be the amount of rows for the amount of nodes,
# and the amount of columns with the number of input
# nodes, simple lin alg maths. 
weightMatrix1 = tf.Variable(tf.zeros([1,4]))

# Seems that we dont need to specify what type the output
# node type will be, as we have done with the others, 
# i.e. .placeholder and .Variable respectively. 
outputNodeValue = tf.matmul(inputNodeValue, weightMatrix1)

# so thus far, we have determined the 
# kind of operations we would like to perform
# and what the matrices and vectors are and look
# like. 
# Next is to define the optimization route, and initiating
# the training loop. 

session = tf.Session()
o = session.run(outputNodeValue, {inputNodeValue:[5]})
print(o)
