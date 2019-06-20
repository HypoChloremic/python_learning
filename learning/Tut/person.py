
# To make it easier, just view the functions as actual functions. This will make stuff much more clear.

class PersonV1:

    def __init__(self, name, job = None, pay = None): # If the default value, if nothing is parsed in when the class is called, one may equate for instance job = None, in order to set the default value.
        self.name = name
        self.job = job # self.job and job are two different variables that happen to have the same name.
        self.pay = pay


class PersonV2:

    def __init__(self, name, job = None, pay = None): # If the default value, if nothing is parsed in when the class is called, one may equate for instance job = None, in order to set the default value.
        self.name = name
        self.job = job # self.job and job are two different variables that happen to have the same name.
        self.pay = pay


    def lasName(self):
        return self.name.split()[-1] # This is putting it into the class the last name feature

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1+percent)) # This removes the necessity to hardcode the raise below. Programming etiquette. 
        
if __name__ == "__main__":
    x = PersonV1("Dude", "hello", "world")
    #print(x.job)
    bob = PersonV1("Bob Blah", job ="dev", pay=100000)
    bob.pay *= 1.1  # What is worth noting here is that bob.pay refers to the variable saved in the object Bob,
                    # structured as a class, which shows some interesting potential for data manipulation!
    #print("%.2f" % bob.pay)
    #print(bob.pay)

    sue = PersonV2("Sue Blah", pay = 8888)
    print(sue.pay)
    sue.giveRaise(.5)
    print(sue.pay)
# In print(".2f" % pay) where %.2f refers to 2 decimal point. Intriguing indeed.
