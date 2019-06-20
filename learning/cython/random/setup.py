from distutils.cores import setup
from Cython.Build import cythonize

setup(ext_moduels=cythonize("l.pyx"))
