# super(base-class, sub-class)

# Python finds MRO for sub-class
# It then finds base-class in that MRO
# It take everything after base-class in the MRO and finds the first class in that sequence with a matching method name


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


print(SortedIntList.mro())
print(super(SortedList, SortedIntList))

# in the case above, super will return a proxy which is the following excerpt of the SortedIntList MRO:
#   SortedIntList   <- this is the first class of the MRO that was used on super()
#   IntList
#   SortedList      <- this is the class from which the proxy will extract the following class as the first class
#   SimpleList      <= this will be the first class of the proxy
#   object          <= this will be the second

# super() will return a proxy which, when asked for the add method, returns add from the SimpleList class
print(super(SortedList, SortedIntList).add)
print()
# since the super above is bound to the class, we can only call directly static methods
try:
    super(SortedList, SortedIntList).add(4)
except TypeError as e:
    print(str(e))

super(SortedIntList, SortedIntList)._validate(5)
try:
    super(SortedIntList, SortedIntList)._validate('hello')
except TypeError as e:
    print(str(e))

# Note that Python raises an exception if the second argument is not a subclass of the first
super(int, IntList)