# iter() has an extended form which accepts two paramenters instead of one
# it is commonly used to produce infinite series
# this is the format: iter(callable, sentinel)
#   callable must not accept arguments and is responsible for producing the values of the series
#   sentinel is the mark that indicates when the iteration must end. When callable produces the sentinel, the iteration
#            stops.

# Simple example of infinite iterator
import datetime

i = iter(datetime.datetime.now, None)
# since None will never be returned by now() function, the iterator will never stop

print(next(i))
print(next(i))
print(next(i))
print()

# reads a file until the END string is found
with open("ending_file.txt", 'rt') as f:
    for line in iter(lambda: f.readline().strip(), 'END'):
        print(line)
