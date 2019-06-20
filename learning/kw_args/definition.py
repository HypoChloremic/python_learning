# Args and kwargs are very interesting indeed

# The following lambda function, can be defined as a(*args): return args
# It will return the arguments which are given to it. What is so interesting
# about arguments is that they are no dictionaries, which implies that they 
# do not need to be parsed as a(open="something") returning {"open":"something"}
# but instead will only provide a tuple; a(open) returns ("open"). 
# providing a ** before the name of the args will create dictionaries
# out of the  

a = lambda *args: args # returns the arguments in a tuple
b = lambda **kwargs: kwargs # returns a list
z = lambda *this_can_be_whatever: this_can_be_whatever
r = lambda **this_can_be_whatever: this_can_be_whatever