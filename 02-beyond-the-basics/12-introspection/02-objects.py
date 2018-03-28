i = 7
# dir can be used to access the attributes of an object
print(dir(i))
print()
# getattr can be used to access the value of an attribute
print(getattr(i, 'denominator'))
print(i.denominator)
print()
print(getattr(i, 'conjugate'))
# since methods are attributes of an object, getattr can access methods as well
print(callable(getattr(i, 'conjugate')))  # we can verify if it is a method using callable function
print(i.conjugate.__class__.__name__)  # builtin_function_or_method
print()
try:
    print(getattr(i, 'index'))
except AttributeError:
    print("i does not have 'index' attribute")  # if the attribute does not existe, getattr raises AttributeError
print()
# to verify f an attribute exists, we can use hasattr function
print(hasattr(i, '__class__'))
print(hasattr(i, 'índex'))