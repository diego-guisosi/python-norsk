# Assertions can be used to test class invariants
# If assertions are degrading performance, we can disable them with -O command line param

from bisect import bisect_left
from collections.abc import Sequence, Set
from itertools import chain


class SortedSet(Sequence, Set):
    """ Class implemented to present some collection protocols """
    def __init__(self, items=None):
        """ set constructor is a good model for SortedSet constructor """
        self._items = sorted(set(items)) if items is not None else []

    def __contains__(self, item):
        try:
            self.index(item)
            return True
        except ValueError:
            return False

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __repr__(self):
        return "SortedSet({})".format(
            repr(self._items) if self._items else ''
        )

    def __eq__(self, other):
        if not isinstance(other, SortedSet):
            return NotImplemented
        return self._items == other._items

    def __ne__(self, other):
        if not isinstance(other, SortedSet):
            return NotImplemented
        return self._items != other._items

    def __getitem__(self, index):
        result = self._items[index]
        return SortedSet(result) if isinstance(index, slice) else result

    def _is_unique_and_sorted(self):
        return all(self[i] < self[i + 1] for i in range(len(self) - 1))

    def index(self, value, start=0, stop=None):
        assert self._is_unique_and_sorted()
        index = bisect_left(self._items, value)
        if (index != len(self._items)) and (self._items[index] == value):
            return index
        raise ValueError("{} not found".format(repr(value)))

    def count(self, item):
        assert self._is_unique_and_sorted()
        return int(item in self)

    def __add__(self, other):
        return SortedSet(chain(self._items, other._items))

    def __mul__(self, rhs):
        return self if (rhs > 0) else SortedSet()

    def __rmul__(self, lhs):
        return self * lhs

    def issubset(self, iterable):
        return self <= SortedSet(iterable)

    def issuperset(self, iterable):
        return self >= SortedSet(iterable)

    def intersection(self, iterable):
        return self & SortedSet(iterable)

    def union(self, iterable):
        return self | SortedSet(iterable)

    def symmetric_difference(self, iterable):
        return self ^ SortedSet(iterable)

    def difference(self, iterable):
        return self - iterable
