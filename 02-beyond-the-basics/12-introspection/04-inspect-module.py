# the inspect module contains advanced tools to introspect modules
import inspect
import sorted_set

print(inspect.ismodule(sorted_set))  # Tests if an object is a module
# getmembers() returns everything in the module namespace as a list of name and value pairs (including all built-ins)
print(inspect.getmembers(sorted_set))
print()

# getmembers() accepts a predicate function as the second argument, which allow us to filter the results. Inspect module
# contains 16 predicates that can be used with getmembers()
print(dir(inspect))
print()
print()
print(inspect.getmembers(sorted_set, inspect.isclass))
# As we can see, get members returned all classes bounded to the sorted_set namespace (this includes the imports)
# "import" binds objects in another module's namespaces to names in our current namespace

# since we have names bound to objects of another modules, we can import imported modules
from sorted_set import chain
print(list(chain([1, 2, 3], [4, 5, 6])))

# chain is a class we imported from itertools to sorted_set and bounded it to sorted_set module namespace
# because of this binding, we can use the binded name as source of the import to other module. This binding acts as if
# the object had been originally defined on sorted_set module

# the code below retrieve all functions of the SortedSet class
print(inspect.getmembers(sorted_set.SortedSet, inspect.isfunction))
print()

# to interrogate individual functions, we can use the signature function
init_sig = inspect.signature(sorted_set.SortedSet.__init__)
print(init_sig)
print(init_sig.parameters)
print(repr(init_sig.parameters['items'].default))  # this will return the default value of "items" parameter

# signature() does not work for all functions. ValueError is raised when trying to access functions natively
# implemented with C