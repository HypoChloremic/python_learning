commandline: python setup.py build_ext --inplace

male sure to save the file you want to use as a pyx
whereas the name of that is then put into ext_modules in the setup 
from the distutil.core.setup()
and we use the cythonize method from the Cython.Build.

Now, this produces a helloworld.pyd. In order to use it, we simply
import it as a normal module with import helloworld