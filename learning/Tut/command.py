import os
import subprocess

os.system(r'C:\Python34\python setup.py build')
#Or
subprocess.call(r'C:\Python34\python setup.py build', shell=True)
