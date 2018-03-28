# extended call sintax


def print_numbers(number, *numbers):
    # passing *numbers to print function will extend the parameters, so each positional argument is passed to print()
    # this function first parameter is mandatory and, the others, are optional
    print(number, *numbers)

print(1, 2, 3)

t = (1, 2, 3)
print_numbers(*t)

# as we can see, it's possible to unpack a tuple into mandatory and *args at the same time


def print_colors(red, green, blue, **kwargs):
    print('r = {}'.format(red))
    print('g = {}'.format(green))
    print('b = {}'.format(blue))
    print(kwargs)


# it is possible to do the same with **kwargs
k1 = {'red': 21, 'green': 68, 'blue': 120, 'alpha': 52}
print_colors(**k1)

# observe that the order of the keys defined on dict does not matter
# python unpacks each key into the function parameter that have the same name of the key
k2 = {'green': 68, 'red': 21, 'blue': 120, 'alpha': 52}
print_colors(**k2)
