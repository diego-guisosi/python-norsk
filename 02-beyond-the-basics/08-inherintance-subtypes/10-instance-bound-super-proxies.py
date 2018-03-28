# super(class, instance-of-class)

# Finds the MRO for the type of the second argument
# Finds the location of the first argument in the MRO
# Uses everything after that for resolving methods

from pprint import pprint as pp

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


class SortedIntList(IntList, SortedList):

    """
    This implementation will keep both IntList and SortedList add behavior
    So, add will sort the elements after each invocation and will not accept anything but Int
    """

    def __repr__(self):
        return "SortedIntList({!r})".format(list(self))


pp(SortedIntList.mro())
sil = SortedIntList([5, 15, 10])
print()
print(sil)

# proxy will resolve to SimpleList.add, bypassing the Int validation and the sorting of the elements
super(SortedList, sil).add(6)
super(SortedList, sil).add("I'm not a number. I'm a free man!!")
print(sil)