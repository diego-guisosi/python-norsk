from math import factorial
from pprint import pprint
import os
import glob

words = "Why sometimes i have believed as many as six impossible things before breakfast".split()

print(words)

lengths = [len(word) for word in words]
print(lengths)

# syntax -> [expr(item) for item in iterable]
# list comprehensions produces new lists, according to the given expression
# the previous comprehension could be implemented as follows:

lengths = []
for word in words:
    lengths.append(len(word))

print(lengths)
print()

# digits length of the first 20 factorials
f = [len(str(factorial(x))) for x in range(20)]
print(f)
print(type(f))

# set comprehensions have the same syntax, but {} must be used instead of []
# removing duplicates of the list comprehension above
s = {len(str(factorial(x))) for x in range(20)}
print(s)
print(type(s))
print()

# dictionary comprehensions have similar syntax
country_to_capital = {'United Kingdom': 'London',
                      'Brazil': 'Brazília',
                      'Morroco': 'Rabat',
                      'Sweden': 'Stockholm'}
print(country_to_capital)

# the comprehension below switch keys and values
capital_to_country = {capital: country for country, capital in country_to_capital.items()}
print(capital_to_country)
print()

# Duplicates: later keys overwrite earlier keys
words = ["Hi", "Hello", "Foxtrot", "Hotel"]
d = {x[0]: x for x in words}
print(d)
print()


# DON'T CRAM TO MUCH COMPLEXITY INTO COMPREHENSIONS
# The example below is the limit accepted
file_sizes = {os.path.realpath(p): os.stat(p).st_size for p in glob.glob("*.py")}
pprint(file_sizes)