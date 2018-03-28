# type function returns the type object of the introspected argument
i = 7
print(type(i))
print(repr(int))
print()
print(type(i) is int)

# since type returns the type of the argument, we can use it to construct objects of the returned type
print(type(i)(99))  # this will create an object of the same type of i -> it is the same of doing int(99)
print()

# the type of the type is type
print(type(type))
print()
# type returns the value of __class__ attribute
print(i.__class__)  # int
print(i.__class__.__class__)  # type
print(i.__class__.__class__.__class__)  # type of type is also type
print()
# we have a cyclic reference between object and type
#   type is a subclass of object
#   object is of type type
print("Type is subclass of object" if issubclass(type, object) else "")
print("Type of object is type" if type(object) else "")
print()
# always prefer issubclass or isinstance to verify the type of an object
print(isinstance(i, int))
