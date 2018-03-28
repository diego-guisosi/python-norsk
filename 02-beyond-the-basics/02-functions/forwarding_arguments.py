# extended call sintax is commonly used to forward all arguments of a function to other functions


def trace(f, *args, **kwargs):
    """ Traces arguments and return values of other functions """
    print("args   = {}".format(args))
    print("kwargs = {}".format(kwargs))
    r = f(*args, **kwargs)
    print("return = {}".format(r))
    return r


print(int("ff", base=16))
print(trace(int, "ff", base=16))

# with this combination of arguments (*args, **kwargs), the function can accept and forward any combination of
# positional and key-value arguments. This way, the trace function works with any other function


def upper_name(name):
    return name.upper()


def lower_name(name, surname):
    return "{} {}".format(name, surname) if surname else name


trace(upper_name, "Diego")
trace(lower_name, "Diego", "Guimaraes")

