def gen123():
    yield 1
    yield 2
    yield 3


# generators are iterators
v = gen123()
print(v)
print(next(v))
print(next(v))
print(next(v))
# print(next(v))  this next call would raise an StopIteration exception

# since generators are iterators, than can be used anywhere iterators are used
for x in gen123():
    print(x)

h = gen123()
i = gen123()

print()
print(h)
print(i)
print(h is i)  # each call to the generator function returns a new generator

print(next(h))
print(next(h))
print(next(i))


def gen246():
    print("About to yield 2")
    yield 2
    print("About to yield 4")
    yield 4
    print("About to yield 6")
    yield 6
    print("About to return")


h = gen246()
next(h)
next(h)
next(h)
next(h)