For interaction between python and the CMD, one is to do the following

import os 

command = "the command, e.g.: start payload.txt"

os.system(command)
os.system(r'also further commands') # the same as the previous os.system(command)?
os.mkdir("something") #will create a directory called something

also the following may work

import subprocess

subprocess.call(r'the command', shell=True)