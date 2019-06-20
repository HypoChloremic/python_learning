# Generators are technically functions
# they generate values which we can access by iterating
# over the generator. The use of this is to avoid 
# saving the values in a list. 
# in stack we are presented with an example
# where we will search for something
# we could either search for the shit
# save the results in a list
# then present them to the user
# On the other hand, with a generator function
# we could display this to the user when doing the 
# operation. 
# The following is provided in the documentation for the update:
# I said, "yield a series of values" because our hypothetical function doesn't 
# "return" in the normal sense. return implies that the function 
# is returning control of execution to the point where the function was called. 
# "Yield," however, implies that the transfer of control is temporary and 
# voluntary, and our function expects to regain it in the future

# "yield is just return (plus a little magic) for generator functions"
# So whenever next() is called on a generator, the generator is 
# responsible for passing back a value to whomever called next().
# It does so by calling yield along with the value to be passed
# back (e.g. yield 7). The easiest way to remember what yield
# does is to think of it as return (plus a little magic) for 
# generator functions.**

def exempel(num = 0):
# Det som är speciellt med yield är att den kommer att skapa en 
# generator när den kallas. Konsekvensen är att när man langar
# next(generator) kommer man att det som yield [statement or whatever]
# ger och pausar där. När den pausar där, kommer den att spara alla values
# den kommer att komma ihåg var i the if statements den är, vad num är osv. 
# När next(generator) kallas igen kommer man att run through tills man 
# hittar nästa yield (om detta är genom att det finns en yield några)
# rader under eller om man kommer tillbaka till samma yield mha en loop!
	yield "wuut"
	while True:
		print("början")
		if num == 4: 
			yield num
			print("eh")
		num += 1
	print("hello world")

a = exempel()
print(next(a))
print(next(a)) 
# If we did this a third time we would hamna in an endless 
# loop, because the generator is trying to find the next 
# yield statement such that it may pause, however 
# it aint able to do so, cuz the yield statement which is there
# is trapped within an if statement with the conditional num == 4
# and as num == 4 is long passed due to the increments,
# it will not stop printing "början"!!  
