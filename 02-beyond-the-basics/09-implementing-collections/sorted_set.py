from bisect import bisect_left
from collections.abc import Sequence, Set
from itertools import chain


class SortedSet(Sequence, Set):
    """ Class implemented to present some collection protocols """
    def __init__(self, items=None):
        """ set constructor is a good model for SortedSet constructor """
        self._items = sorted(set(items)) if items is not None else []

    # Container protocol
    # Permits the use of "in" and "not in" infix operators
    def __contains__(self, item):
        # the line bellow was the implementation before of index() O(log n) implementation
        # return item in self._items
        try:
            self.index(item)
            return True
        except ValueError:
            return False

    # Sized protocol
    # Permits the use of "len()" function
    def __len__(self):
        return len(self._items)

    # Iterable protocol
    # Permits the collection to be used in loops
    def __iter__(self):
        # It is important to remember that generator functions are functions that returns generators and, generators,
        # are iterators. So, we could have used a generator as the return value.
        # e.g: for item in self._items:
        #         yield item
        return iter(self._items)

    # Representation protocol
    # Gives a more detailed representation of the object.
    # It is usually a representation that lets us to reconstruct the object
    def __repr__(self):
        return "SortedSet({})".format(
            repr(self._items) if self._items else ''
        )

    # Equality protocol
    # Permits objects to be equality compared by value instead of by reference (default implementation)
    def __eq__(self, other):
        # It is important to return NotImplemented instead of raise NotImplementedError
        if not isinstance(other, SortedSet):
            return NotImplemented
        return self._items == other._items

    # Inequality protocol
    # Although the default implementation of __ne__ is the negation of __eq__, Python documentation recommends to always
    # implement __ne_ if __eq__ is provided
    def __ne__(self, other):
        if not isinstance(other, SortedSet):
            return NotImplemented
        return self._items != other._items

    # Sequence protocol: indexing and slicing
    # Permits accessing elements by indexes within []
    def __getitem__(self, index):
        # Sequence protocol: slicing
        # getitem index argument cab be of type int or slice(start, stop, step)
        result = self._items[index]
        return SortedSet(result) if isinstance(index, slice) else result

    # Sequence protocol: reversed
    # if __getitem__ and __len__ are implemented, __reversed__ default implementation fallbacks to them and returns
    # an iterator that access elements with negative indexes (based on __len__)
    # this default behavior attends our needs. So, it will be kept this way

    # Sequence protocol: index (no special method) -> index = seq.index(item)
    # Permits consulting the index of the element provided as parameter
    # index() must return the the positive index of the first element found in the collection or a negative index
    # if the element is not found. We could implement this based on __getitem__
    # This function implementation will be provided by the Sequence Abstract Base Class (from collection.abc) though.
    # Abstract Base Classes can be used to tag a particular class as being an implementation of a particular interface
    # e.g.: if SortedSet inherits from Container (ABC), it must implement __contains__ and then we could test if
    # SortedSet is of type Container
    # Some ABCs provide default implementation to methods, if mandatory abstract methods are implemented
    # Sequence ABC inherits from Sized, Iterable and Container ABCs, but only demands implementation of the special
    # methods __getitem__ and __len__. If both of these methods are implemented, Sequence ABC provides default
    # implementation to __contains__, __iter__, __reversed__, index() and count() methods
    # Although index is provided by the ABC, we will implement a faster algorithm one, since ABC's implementation
    # does not know that this collection is a Set and will not have duplicates
    # The default index() implementation is of liner time complexity O(n). The implementation we will provide is of
    # logarithmic running time complexity O(log n)
    def index(self, value, start=0, stop=None):
        index = bisect_left(self._items, value)
        if (index != len(self._items)) and (self._items[index] == value):
            return index
        raise ValueError("{} not found".format(repr(value)))

    # Sequence protocol: count (no special method) -> num = seq.count(item)
    # Permits access to the number of occurrences of some element in the collection
    # count() implementation will also be inherited from Sequence Abstract Base Class (from collection.abc), but we
    # will not use it, since the default implementation does not consider that our collection is a Set and will not
    # have duplicated elements. count() will make use of index() O(log n) time complexity implementation
    def count(self, item):
        return int(item in self)

    # Sequence protocol: concatenation (__add__)
    # Permits the use of the infix concatenation operator +
    # Although a concatenation operation does not make much sense in a Set, we will implement it as an union set
    # operation to show how it works
    def __add__(self, other):
        # to avoid intermediate set constructions, we will not construct a set to each SortedSet parameter and
        # a third one as the product of of executing set(self).union(set(other))
        # itertools.chain allows us to stream all the elements from one operand and then the other into the SortedSet
        # constructor
        return SortedSet(chain(self._items, other._items))

    # Sequence protocol: repetition (__mull__ and __rmul__)
    # For lists, works like repeated concatenation of the original list
    # For sets, this also does not makes sense. So, our implementation will return a the same instance of the SortedSet
    # containing all original elements or and empty SortedSet, if the multiplicand is lesser than one
    # if the class is being used as the left side operand, python will delegate the repetition to __mul__
    # if the class is being used as the right side operand, python will delegate to __rmul__
    def __mul__(self, rhs):
        # rhs is an acronym to right hand side
        return self if (rhs > 0) else SortedSet()

    def __rmul__(self, lhs):
        # lhs is an acronym to lhs
        # we will only delegate to __mul__
        return self * lhs

    # Set protocol:
    # According to the Abstract Base Class documentation, Set ABC inherits from Sized, Iterable and Container
    # and must provide implementation to the abstract special methods __contains__, __iter__ and __len__ to
    # implement Set protocol. This will give us the implementation of all relational operators and
    # isdisjoint method as well
    # ABC Set only provide implementation to the infix operators. If we want the set named methods equivalent, we
    # must implement then ourselves. But it is easy to implement using the infix operators
    #
    # Relational Operators
    # special method(*)     infix operator      set method(**)      meaning
    # __le__()              <=                  issubset()          subset
    # __lt__()              <                                       proper subset
    # __eq__()              ==                                      equal
    # __ne__()              !=                                      not equal
    # __gt__()              >                                       proper superset
    # __ge__()              >=                  issuperset()        superset
    #                                           isdisjoint()*
    #
    # Algebraic operators (bitwise operators)
    # special method(*)     infix operator      set method(**)
    # __and__()             &                   intersection()
    # __or__()              |                   union()
    # __xor__()             ^                   symmetric_difference()
    # __sub__()             -                   difference()
    #
    #  * Provided by collections.abc.Set
    # ** As implemented by built-in set
    #
    # The difference between the operator and the set methods version is that operators only accept operands of the same
    # type, while methods accept any iterable series as argument
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
