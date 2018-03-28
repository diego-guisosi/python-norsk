# decorators are callables that receive a callable as parameter and return a callable
# the returned callable is binded to the same name of the decorated function
# they can be used to modify function behavior, without having to change the implementation of the function that must
# be modified


def escape_unicode(f):
    def wrap(*args,**kwargs):
        x = f(*args, **kwargs)
        return ascii(x)

    return wrap

@escape_unicode
def northen_city():
    return "Tromsó"


if __name__ == '__main__':
    print(northen_city())