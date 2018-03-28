# Classes can be applied as decorators (since they are callables), but only if the class creates an callable instance
# Applying a class as decorator creates a new instance, which will be initialized by __init__ and will after have its
# __call__ method called


class CallCount:
    def __init__(self, f):
        self.f = f
        self.counter = 0

    def __call__(self, *args, **kwargs):
        self.counter += 1
        return self.f(*args, **kwargs)


@CallCount
def hello(name):
    print("Hello, {}".format(name))


if __name__ == '__main__':
    hello("John")
    hello("Yoko")
    print(hello.counter)
