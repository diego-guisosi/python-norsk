# MRO: ordering that determines method name lookup

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


# Method Resolution Order can be verified through the class attribute __mro__, which is a tuple containing the classes
# in the order that the method names will be resolved
print(SortedIntList.__mro__)
# we can also access the same information with the function mro(). The function returns a list though
print(SortedIntList.mro())

# How is MRO used ?
# When a METHOD of an INSTANCE of SOME CLASS is called (e.g: obj.method()), python verifies, in order,
# the classes present on MRO until it finds the method. The first class having a method that matches the name is called


class A:
    def func(self):
        return 'A.func'


class B(A):
    def func(self):
        return 'B.func'


class C(A):
    def func(self):
        return 'C.func'


class D(B, C):
    pass


class E(C, B):
    pass


print(D.mro())
print(D().func())
print()
print(E.mro())
print(E().func())

# this does not explain how SortedIntList is also sorting elements after add() call. Since IntList will be the
# first class having a method name that matches add(), only the validation of integers should be done
