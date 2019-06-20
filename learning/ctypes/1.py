import subprocess
from ctypes import *
k = "loop.so"
ks = "loop.o"

# This subprocess command is run to compile the library necessary
# for us to run for the program. 
# subprocess.call("gcc -shared -o forloop.so -fPIC forloop.c", shell=True)

l = CDLL("loop.so")
def f():
	return l.main()