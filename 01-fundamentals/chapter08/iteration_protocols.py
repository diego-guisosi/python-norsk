iterable = ["Spring", "Summer", "Autumn", "Winter"]
iterator = iter(iterable)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

#this last one would throw StopIteration exception
#print(next(iterator))


def first(iterable):
    try:
        iterator = iter(iterable)
        return next(iterator)
    except StopIteration:
        raise ValueError("iterable is empty")


# since only the protocol built-in functions are being used, "first" will work with any iterable
print(first(["1st", "2nd", "3rd"]))
print(first(("1st", "2nd", "3rd")))
print(first({"1st", "2nd", "3rd"}))  # since set is unordered, the first element can be any of the three elements

first(set())