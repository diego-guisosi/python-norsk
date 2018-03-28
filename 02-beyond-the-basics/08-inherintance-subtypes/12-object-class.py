# object class is the core of the Python object model
# object is the ultimate base class of every class
# object is automatically added as a base class

class NoBaseClass: pass
print(NoBaseClass.__bases__)
print(dir(object))

# object does significant work to tying Python's implementation details
# we can see that object have as attributes only "dunder (double underscore)" functions
# object provides the default implementation of all these special methods

# Hookes on Python's comparison operators
#   __eq__
#   __ge__
#   __gt__
#   __le__
#   __lt__
#   __ne__
#
# String and representations
#   __str__
#   __repr__
#
# Mechanisms for basic attribute lookup and management (forms the foundation on which Python exposes
# attributes to callers)
#   __getattribute__
#   __setattr__
#   __delattr__