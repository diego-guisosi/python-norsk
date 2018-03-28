# filter can be used to remove elements of iterables that does not match the predicate function provided
# filters accept only a single input sequence

positives = filter(lambda x: x > 0, [1, -5, 0, 6, -2, 8])
print(list(positives))

# passing None to the predicate function will cause filter to remove all iterable elements that evaluate fo False
trues = filter(None, [0, 1, False, True, [], [1, 2, 3], '', 'hello'])
print(list(trues))


# map and filter on Python 2 are eagerly evaluated and generate lists. This is a lot different of the lazy behavior
# that we have with Python 3