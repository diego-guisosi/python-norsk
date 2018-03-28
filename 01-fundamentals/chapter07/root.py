def my_function(x):

    if x < 0:
        raise ValueError("x can not be negative")

    print(x)


my_function(10)
my_function(-1)