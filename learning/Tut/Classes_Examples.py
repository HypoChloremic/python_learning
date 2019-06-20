'''class Test:
    pass #'Just skip past this python'

x = Test()

Self will be referring to anything that is its
own functions or variables (e.g. This function is attached
to me, or this is my function). Make sure that the
word self is used within the arguments of the function


class ph:
    def printHam(self): #first argument is self
        print("ham")

x=ph()
x.printHam()



A Constructor, or initialization function, it is a function
which is called when a class is created (any defaults
would be provided here).


class ph:
    def __init__(self):
        self.y = 5
        self.z = 10
    def printHam(self):
        print("ham")

x = ph()
x.printHam()

print(x.y)
print(x.z)
'''

class ph:
    def __init__(self):
        self.y = 5
        self.printHam()
    def printHam(self):
        print("ham")

x = ph()
x.printHam()

print(x)
print(x)

