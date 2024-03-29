# Regex

## Assertions
```python
import re

# An assertion: an assertion is defined as the following: '(?= . . .)' where ?= and the parenthesis are used.
# Assertions give up the match, and only return match or no match! it is almost binary boolean in nature. 
# So what is inside the (?= ...) will not be highlighted, i.e. matched. 
# Assertion: asserting presence of pattern

# POSITIVE: the assertion IS present
# 'Look-BEHIND' assertion: is using `<=` instead of `=` in the assertion, i.e. (?<= ...)
# The look-behind assertion refers to identifying an assertion 
# (which does not highlight, instead just matched boolean wise, binary
# if it is there or not) BEFORE an expression. 
# Behind: (?<=  ), is preceeding our pattern.

# 'Look-AHEAD' is with `?=` (I guess searching for something behind...?)
# Ahead: this succeeds our pattern of interest

# Example:

t1 = '1: Hello there 2: World here'
re.search(r'(?<=\d:\W)([a-zA-Z\W]+)')
# will highlight the text after '1: '
# Several things is occurring:
# 1) Look-behind: (?<=\d:\W) which is saying that our pattern comes after a single digit ('\d'), a colon(':') and a whitespace ('\W')
# 2) our pattern inside the (...) which doesnt have the assertion parameter '?=' indicates that we are searching for:
# 2a) a-z any character a-z lowercase
# 2b) or A-Z any character A-Z uppercase
# 2c) or \W any non-character (e.g. whitespace) character
# 2d) grouped together, making them all or between each other with the hard brackets '[...]'
# 3e) '+' single or more of the stuff inside the brackets!

# NEGATIVE: the assertion is NOT persent
# negative look-behind: '(?<!  ...)' so instead of an '=' sign we get a '!' sign. 
# negative look-ahead: '(?! ...)'
```



### Matching in the beggining and end

Assume a vector of strings. We would like to match the strings which start with `Endo` and end with either `-` or `+`:

```python
import re
vec = ['Endo asdas +', 'Endo asdas -', 'ndo asdas +', 'Endosfeaac +', ]
# to match these we can do the following:
re.match(r"(?=.*Endo).*(?<=[+-])")
```

First we added `.*` to the look-ahead assertion before putting Endo there, because we are saying that it should look through anything before the assertion to match the pattern. Furthermore we added `.*` in the main pattern claiming that it should highlight the entire subsequent string. Finally we have `?<=[+-]` for the look-behind, which tells that the pattern should end with either one `+ or -`.

## Modifiers

1. ***Single line [s]*** - Allows the . metacharacter (which matches everything except newlines) to match newlines too
2. ***Multi-line [m]*** - ^ and $ now match the beginning/end of lines, rather than default behavior of matching beggining/end of entire string
3. ***Insensitive [i]*** - Upper and lower-case characters are matched, e.g. A = a [This is a great one]
4. ***Extended [x]*** - Ignores whitespace. To include spaces, they must be escaped using \. Also allows comments inside the regex with #
5. ***ASCII [a]*** - Match to ASCII-only characters, rather than the full Unicode character set

### Use modifiers

#### Bitwise
To use modifiers: 

```python
import re
t1 = '1: Hello 2: There'
re.match('[a-zA-Z]+', t1, re.S|re.I)
```

Note that the BITWISE OR (`|`) in python to add different modifiers for the regex modifier flags. 

#### Inline modifier
One adds the flags after the `?` in `(?...)` e.g. re.match('(?si)[a-z]+', ...) where the flags `s` and `i` are used. 


### Case insensitivity
the `i` flag offers a nice opportunity to make syntax easier, because [a-zA-Z] is not necessary, but just [a-z] | [A-Z] suffices with the `i` flag.


# Numpy
## Difference between to sets
Assume to numpy arrays with strings, and we wish to find the difference:

```python
a,b = np.array([...]), np.array([...])
np.setdiff1d(a,b) # will return that difference
```


# Python lists 
## Reversing list

```python
a = ['a','b', 'c']
r = [i for i in reversed(a)] # = ['c', 'b', 'a']

# Tar files
Tar files are is a file format designed to aggregate multiple files under one umbrella file, with the `.tar` file-extension. 
## Reading tar-files in python
To read a tar file in python, the `tarfile` module can be used.

​```python
import tarfile as tf
with tf.open(f'{file_name}.tar', 'r') as tfile:
	tf.getnames() # this will return the names of the files inside the tar file
	tf.getmembres() # seemingly returns the object members of the tar file. 
	tf.extractall(member, path='.') # Will extract the tar file to the given path
									# Note that 'member' is not needed.
```

## Closing tarfile
remember that the `tarfile` module does not have a `__enter__` and `__exit__`, which in turn implies that the `with` statement will not close the tarfile. 
To close:

```python
import tarfile as tf
with tf.open('file.tar', 'r') as tfile:
	tfile.extractall()
tfile.close()
```

# gzip
## reading a gzip file
The `gzip` module is used extensively here:
````python
import gzip
with gzip.open('gile.gzip', 'r') as file:
	for line in file:
		print(line)

````

# Decorators

## Basics

```python
import functools

def decorator(func):
    
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # ...
        
        value = func(*args, **kwargs)
        
        # ...
        return value
    
    return wrapper_decorator
```

## Decorators inside classes

```python
import functools
class SomeClass:
    def Decorator(func):
        @functools.wraps
        def wrapper(self, *args, **kwargs):
            #...
            returned = func(self, *args, **kwargs)
            #...
            return returned
        return wrapper
    
    @Decorator
    def some_func(self, ..., ...):
        return "blabla"
```

Note how we isolate the `self` argument when creating the `Decorator()`. This such that we may access the self keyword of the class, and all of the associated objects, when using the `Decorator`. 

# Virtualenv

To use Python virtual environments (virtualenv) in Linux, follow these steps:

1. Open a terminal window.

2. Install `virtualenv` package if you don't have it already. Run the following command:

   ```
   Copy code
   pip install virtualenv
   ```

3. Create a new virtual environment. Navigate to the desired directory and run the following command:

   ```
   Copy code
   virtualenv myenv
   ```

   Replace `myenv` with the desired name for your virtual environment.

4. Activate the virtual environment by running the activation script. Use the following command:

   ```
   bashCopy code
   source myenv/bin/activate
   ```

   Once activated, you should see the name of the virtual environment `(myenv)` at the beginning of the command prompt.

5. Install packages and work with your Python project as usual. Any packages you install will be isolated within the virtual environment.

6. When you're done working within the virtual environment, you can deactivate it. Simply run the following command:

   ```
   Copy code
   deactivate
   ```

   The virtual environment will be deactivated, and you will return to your system's default Python environment.

Using a virtual environment allows you to isolate dependencies for different projects, avoiding conflicts and ensuring project-specific package versions. You can create and activate multiple virtual environments as needed for different projects.