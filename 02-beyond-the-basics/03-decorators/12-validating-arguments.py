# A common use for decorators is to validate function arguments


def check_non_negative(index):
    """ Function that creates a decorator called validator. """
    # check_non_negative itself is not a decorator. It's a function that creates a decorator called validator
    def validator(f):
        """ That is the decorator that validates non-negative arguments by position """
        def wrap(*args):
            if args[index] < 0:
                raise ValueError(
                    'Argument on position {} of the function {} must be non-negative'.format(index, f.__name__)
                )
            return f(*args)
        return wrap
    return validator


@check_non_negative(1)
def create_list(value, size):
    return [value] * size


if __name__ == '__main__':
    print(create_list(1, 3))
    create_list(2, -1)

# It is important to remember that there is no such thing as passing arguments other than callables to decorators.
# To do that, we need to pass the argument to functions that creates decorators. The argument passed to this function
# can be kept by the wrapped function as a closure
