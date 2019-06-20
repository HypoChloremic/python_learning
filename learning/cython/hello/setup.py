from distutils.core import setup
from Cython.Build import cythonize

setup(name="hello world app", ext_modules=cythonize("fib.pyx"))
