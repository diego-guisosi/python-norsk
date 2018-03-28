# isinstance can be used to verify during runtime if an object is of an specific type


class SimpleList:

    def __init__(self, items):
        self._items = list(items)

    def add(self, item):
        self._items.append(item)

    def __getitem__(self, index):
        return self._items[index]

    def sort(self):
        self._items.sort()

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return "SimpleList({!r})".format(self._items)


class SortedList(SimpleList):

    def __init__(self, items=()):
        super().__init__(items)
        self.sort()

    def add(self, item):
        super().add(item)
        self.sort()

    def __repr__(self):
        return "SortedList({!r})".format(list(self))


print(isinstance(3, int))
print(isinstance('string', str))
print(isinstance(1.23, bytes))
print()
# isinstance can be used to verify if an object is a subclass of the given type argument
sl = SortedList([3, 2, 1])
print(isinstance(sl, SimpleList))
print(isinstance(sl, SortedList))
# isinstance accepts a tuple as the second argument and returns true if the object matches any of the tuple elements
x = []
print(isinstance(x, (float, dict, list)))


class IntList(SimpleList):

    def __init__(self, items=()):
        for x in items:
            self._validate(x)
            super().__init__(items)

    @staticmethod
    def _validate(x):
        if not isinstance(x, int):
            raise TypeError('IntList only supports integer values.')

    def add(self, item):
        self._validate(item)
        super().add(item)

    def __repr__(self):
        return 'IntList({!r})'.format(list(self))


print()
il = IntList([1, 2, 3, 4])
il.add(19)
print(il)
il.add('5')