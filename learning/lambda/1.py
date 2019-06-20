# Aight, it seems that lambda is another way of writing functions, i.e. there are two ways of writing these
# either by def or with lambda. If we look at the function below, where we are returning the lambda function, it implies
# that the main function itself will maybe be considered as the lambda function, where we are putting in the variable n, which 
# is considered as an existing variable, we need to declare the variable with other words, by writing "a=make(n)" we are making a the
# function itself, because if we print a, we will be getting a function object, which is true, because it would be equal to writing the following
# 
# def make(n):
# 		def something(k):
# 			pass
# 		return something(2)
# is the same as writing
# def make(n):
# 		return lambda k: None; note that we have k here, where the input k will be the same as def something(k). 



def make(n):
	return lambda x: print(x+n**2)

a = make(5) # Now we are declaring the integer variable in the function, making it accessible for the lambda function 
a(2) # Here we are giving the lambda function, x which is the inpute value i.e. 