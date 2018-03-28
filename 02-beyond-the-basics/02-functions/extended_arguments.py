# extended arguments sintax
def my_function(*args, **kwargs):
    # *args stores arguments positionally into a tuple
    # **kwargs stores key-value arguments into a dictionary
    print("type: {} -> args: {}".format(type(args), args))
    print("type: {} -> kwargs: {}".format(type(kwargs), kwargs))


my_function(1, 2, 3, four=4, five=5)

# extended arguments can have any name, but if the both positional and key-value pairs are necessary,
# key-value arguments must always be defined after positional arguments

# passing dict or tuples references to my_function works
my_positional_params = (3, 2, 1)
my_key_value_params = {'zero': 0}

my_function(my_positional_params, my_key_value_params)