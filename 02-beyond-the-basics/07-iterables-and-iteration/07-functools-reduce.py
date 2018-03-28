# functools.reduce() repeatedly apply a function to the elements of a sequence,
# reducing them to a single value

from functools import reduce
import operator

# The standard library operator module contains function equivalents of the infix operators
# a + b is equivalent to operator.add(a, b)
rslt = reduce(operator.add, [1, 2, 3, 4, 5])
print(rslt)

# the reduce operation below is the same as the following
numbers = [1, 2, 3, 4, 5]
accumulator = operator.add(numbers[0], numbers[1])
for item in numbers[2:]:
    accumulator = operator.add(accumulator, item)
print(accumulator)


# the get an idea of how reduce is calling the function
def mul(x, y):
    """
        x is the interim result (accumulated between function executions)
        y is the next value
    """
    print('mul {} {}'.format(x, y))
    return x * y

reduce(mul, range(1, 10))

# if an empty sequence is passed to reduce, it raises a TypeError
# if only one element is passed to reduce, reduce returns the passed element, without executing the passed function
print()
print(reduce(mul, [1]))

# an optional value can be provided to be the first element of the iterable passed as argument
# so, if the sequence does not have value, the optional value will be immediately returned by the reduce function and
# the accumulator function will not be called. If the sequence has elements, the optional value is added to the
# beginning of the sequence. Optional values are usually used when we are not sure whether the iterable has elements
print()
values = [1, 2, 3]
print(reduce(operator.add, values, 0))
values = []
print(reduce(operator.add, values, 0))
values = [1, 2, 3]
print(reduce(operator.mul, values, 1))