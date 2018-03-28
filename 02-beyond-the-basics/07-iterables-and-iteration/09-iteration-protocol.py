# Iterable and Iterator Protocols
#
# Iterable protocol demands __iter__ implementation, which is responsible to return an instance of iterator
# Iterator protocol demands __iter__ and __next__ implementation.
#   __iter__ must return the iterator itself
#   __next__ must return the next element of the iterator or raise StopIteration exception when the iterator reaches the
#            end of the collection


class ExampleIterator:

    def __init__(self):
        self.index = 0
        self.data = [1, 2, 3]

    def __iter__(self):
        """
        Iterators must implement __iter__ protocol, which is responsible for returning an iterator for the given object
        The most common __iter__ implementation for an iterator is returning of the iterator itself
        """
        return self

    def __next__(self):
        """
        Iterators must implement __next__ protocol as well, which must return the next element of the iterator or
        raise StopIteration exception when the iterator has no more elements to return
        """
        if self.index >= len(self.data):
            raise StopIteration()
        rslt = self.data[self.index]
        self.index += 1
        return rslt


i = ExampleIterator()
print(next(i))
print(next(i))
print(next(i))
try:
    print(next(i))
except StopIteration as e:
    print("StopIteration raised!")

# since we have an iterator, we can use it in a for loop
for i in ExampleIterator():
    print("forloop -> {}".format(i))
