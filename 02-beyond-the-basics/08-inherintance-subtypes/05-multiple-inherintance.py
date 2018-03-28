# Multiple Inherintance
# Method Resolution Order (MRO) and super() function. How this function really works


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


sil = SortedIntList([42, 23, 2])
print(sil)

try:
    sil.add(1.5)
except TypeError as e:
    print(str(e))


# If a class:
#       A. Has multiple base classes
#       B. defines no initializer
# then:
#       ONLY the initializer of the FIRST base class will be automatically called
#
#
class Base1:
    def __init__(self):
        print("Base1.__init__")


class Base2:
    def __init__(self):
        print("Base2.__init__")


class Sub(Base1, Base2):
    pass


Sub()  # Only Base1.__init__ will be called. We can use super() to decide how the initializers should be called

print()
# __bases__ is a tuple provided by classes that can be used to verify which base classes some class inherits from
print(SortedIntList.__bases__)  # will print the tuple containing the base classes in order which they were defined
print(IntList.__bases__)
