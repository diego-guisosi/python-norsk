# Python provides two functions to exam scopes
# globals() returns the the global scope, which contains the global variables of the program
print(globals())
a = 42
print(globals())  # as we can see, "a" has been bounded to the global scope with the value 42
# since globals() returns the global scope, we can assign variables to it as follows:
globals()['tau'] = 6.283185
print(tau / 2)  # this works because we assigned tau to the global scope
print()

# locals() returns the local scope. If we execute it outside any function, we will have the same result of globals()
print(locals() == globals())
print()


# to see locals in action, we will create a local scope by defining a function
def report_scope(arg):
    from pprint import pprint as pp
    x = 496
    pp(locals(), width=10)


report_scope(42)
print()

name = "Joe Bloggs"
age = 28
country = "New Zealand"

# since functions allow arguments expansion also from dictionaries, we might do the following
print("{name} is {age} years old and is from {country}".format(**locals()))
# this is not recommended though, since we would have a hard time to debug
