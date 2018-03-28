class MyClass:
    pass


class MyOtherClass:

    def __init__(self):
        self._counter = 0

    def __call__(self):
        self._counter += 1
        print("I've been called {} time(s)".format(self._counter))


def my_function():
    pass


print("my_function is callable ? {}".format(callable(my_function)))
print("MyClass is callable ? {}".format(callable(MyClass)))
print("MyClass instance is callable ? {}".format(callable(MyClass())))
print("MyOtherClass instance is callable ? {}".format(callable(MyOtherClass())))

# if the object is callable, it can be called like a function
instance = MyOtherClass()
# instance() is just a shorthand to instance.__call__()
# instance callables can be used to create functions that keep state
instance()
instance()
instance()

# all classes are callable. That's why whe can call them like this: MyClass()
# __call__ implementation of classes call the constructor

# since classes are objects themselves, they can be be assigned to variables. Take a look at the next funtion


def my_factory(is_callable=False):
    return MyClass if not is_callable else MyOtherClass


clazz_callable = my_factory(is_callable=True)
clazz_non_callable = my_factory()

print("tyoe of clazz_callable: {}".format(type(clazz_callable)))
print("tyoe of clazz_non_callable: {}".format(type(clazz_non_callable)))
clazz_callable()()

# first () instantiates MyOtherClass and second () calls instance __call__