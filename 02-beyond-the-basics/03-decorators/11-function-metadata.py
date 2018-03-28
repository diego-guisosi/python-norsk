# when functions are decorated, they loose metadata information after de binding of the returned callable to the
# decorated function name

import functools


def noop(f):
    def noop_wrap():
        return f()
    return noop_wrap


def noop_assign(f):
    def noop_wrap():
        return f()

    noop_wrap.__name__ = f.__name__
    noop_wrap.__doc__ = f.__doc__

    return noop_wrap


def noop_wraps(f):
    @functools.wraps(f)
    def noop_wrap():
        return f()
    return noop_wrap


def hello():
    """ Print a well-known message. """
    print('Hello, world!')

@noop
def hello_2():
    """ Print a well-known message. """
    print('Hello, world!')


@noop_assign
def hello_3():
    """ Print a well-known message. """
    print('Hello, world!')


@noop_wraps
def hello_4():
    """ Print a well-known message. """
    print('Hello, world!')


if __name__ == '__main__':
    print(hello.__name__)
    print(hello.__doc__)
    print()
    print(hello_2.__name__)
    print(hello_2.__doc__)
    print()
    print(hello_3.__name__)
    print(hello_3.__doc__)
    print()
    print(hello_4.__name__)
    print(hello_4.__doc__)
