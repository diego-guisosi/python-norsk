sizes = ["small", "medium", "large"]
colors = ["lavender", "teal", "burnt orange"]
animals = ["koala", "platypus", "salamander"]


def combine(size, color, animal):
    return "{} {} {}".format(size, color, animal)

# we can pass as many argumemnts as the argument function needs
# map will get all first elements and pass them to the argument function, then the second elements, third etc.
# the iteration stops when some of the collections reach the last element (even if the other collections already
# have elements
print(list(map(combine, sizes, colors, animals)))


import itertools


def other_combine(quantity, size, color, animal):
    return "{} x {} {} {}".format(quantity, size, color, animal)

# the itertools.count() generates an infinity sequence, but map function stops when the any iterable passed as parameter
# reaches the last element
list(map(other_combine, itertools.count(), sizes, colors, animals))