class ExampleIterator:

    def __init__(self, data):
        self.index = 0
        self.data = data

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


class ExampleIterable:

    def __init__(self):
        self.data = [3, 6, 9]

    def __iter__(self):
        return ExampleIterator(self.data)


for i in ExampleIterable():
    print(i)

print()
[print(i) for i in ExampleIterable()]