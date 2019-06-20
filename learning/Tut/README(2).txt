"""
In the folder containing the .py file to be converted to an exe, create a new .py file, named "setup.py"

write the following: 

"""

from cx_Freeze import setup, Executable


setup(name="something",
          version="some version number",
          executables = [Executable("something.py")])