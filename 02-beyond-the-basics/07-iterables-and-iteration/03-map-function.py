# functional-style programing in python
# map returns an iterator that lazily transforms a given iterable, according to the function passed as parameter


class Trace:

    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print("Calling {}".format(f))
            return f(*args, **kwargs)
        return wrap


codepoints = map(Trace()(ord), "The quick brown fox")
print(codepoints)

# since codepoints is a lazy iterator, the function that transforms the iterable elements will only be called
# if the next element is requested
print(next(codepoints))
print(next(codepoints))
