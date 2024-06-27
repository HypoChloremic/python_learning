# Pythonic code, Raymond Hettinger

### Creating pythonic code

#### PEP8

#### Recurring setup and teardown logic

* When there is recurring setup and teardown logic, use the `with` statement
* This implies the implementation of `__enter__` and `__exit__` in the class statements. 
* We should therefore build a ***context manager*** to use the with statement

#### Where package imports make single module

Sometimes we can find the following:

```python
import jnettools.tools.element.NetworkElement
import jnettools.tools.Routing
import jnettools.tools.RouteInspector
```

These package imports are non-pythonic. Instead we should a ***single module*** such that it is easier to import everything. 

#### Looping over sequences by index

Consider the following example code

```python
num_routes = routing_table.getSize()
for RToffset in range(num_routes):
	route = routing_tagble.getRouteByIndex(RToffset)
	name = route.getName()
	ipaddr = route.getIPAddr()
```

Here we see several aspects that can be corrected and fixed. 

* `.getSize()`: Whenever we are getting somethings size, we should implement the `len` function instead
* `.getRouteByIndex(RToffset)`: we should never make a function call where we provide the index of something. Instead we should implement the square brackets `[...]` functionality.
* `.getName` or `.getIPAddr`: these should be properties instead of function calls. 

##### Sequences

Anything that can be looped over with an index, raises IndexError if looped too far and can do a `len` on is a `sequence`

* These are sequences in python
  * strings
  * lists
  * ...
* These have a common propety:
  * they are `iterables`



### The adapter pattern

When there non-pythonic packages, we can write an adapter class. 

#### Rules of the pattern

* Avoid unnecessary packaging, in favour of simpler imports
* create custom exceptions
* use properties instead of getter methods
* create a context manager for recurring set-up and teardown logic
* use magic methods
  * `__len__`: instead of `getSize()`
  * `__getitem__`: instead of `getRouteByIndex()`
  * make the table iterable
* add a good `__repr__` for better debuggability



#### Example

We have a java-based package that has complex import structure, that we crate an adapter module for. 

First we create an exception related to the NetworkElement module, or class in this case. 

```python
import jnettool.tools.element.NetworkElement
import jnettool.tools.Routing

class NetworkElementError(Exception):
	pass

class Route(object):
    def __init__(self, old_route):
        self.old_route = old_route
    
    @propety
    def name(self):
        return self.old_route.getName()
    
    @property
    def ipaddr(self):
        return self.old_route.getIPAddr()
```





```python
class RoutingTable(object):
    def __init__(self, oldrt):
        self.oldrt = oldrt
    
    def __len__(self):
        return self.oldrt.getSize()
   	
    def __getitem__(self, index):
        if index >= len(self):
			raise IndexError
        return Route(self.oldrt.getRouteByIndex(index))
```



```python
class NetworkElement(object):
	def __init__(self, ipaddr):
		self.ipaddr = ipaddr
		self.oldne = jnettool.tools.elements.NetworkElement()
       
    @property
    def routing_table(self):
        	try:
                return RoutingTable(self.oldne.getRoutingTable())
            except jnettool.tools.elements.MissingVar:
                raise NetworkElementError("No routing table found")
	
    def __enter__(self):
        	return self
    
    def __exit__(self):
        if exctype == NetworkElementError:
            logging.exception('No routing table found')
           	self.oldne.cleanup('rollback')
        else:
            self.oldne.cleanup('commit')
        self.oldne.disconnect()
    
    def __repr__(self):
        return f'{self.__class__.__name__, self.ipaddr}'
```

### namedtuples

Example problem

```python
p = (170, 0.1, 0.6)
if p[1] >= 0.5: 
    print("That is bright")
if p[2] >= 0.5:
    print("Wow, that is light")
```

The code has predictable behaviour, however, we do not know its purpose. We can change it:

```python
from collections import namedtuple
Color = namedtuple("Color", ['hue', 'saturation', 'luminosity'])
p = Color(170, 0.1, 0.6)

if p.saturation >= 0.5:
	print("That is bright")
if p.luminosity >= 0.5:
	print("That is light")
```

