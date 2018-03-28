import reprlib

# reprlib contains a repr functions that can be used as a replacement for the built-in repr
# a common use of reprlib.repr is to avoid printing an entire collection, if it has a large number of elements


class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '{point.x}, {point.y}'.format(point=self)

    def __repr__(self):
        return 'Point2D(x={}, y={})'.format(self.x, self.y)

    def __format__(self, format_spec):
        if format_spec == 'r':
            return '(({}, {}))'.format(self.y, self.x)
        else:
            return '(({}, {}))'.format(self.x, self.y)


if __name__ == '__main__':
    l = [Point2D(x, y) for x in range(1000) for y in range(1000)]
    print(len(l))
    print('{}'.format(reprlib.repr(l)))

    # if we have not used reprlib.repr() function, all one million elements would have been printed
    #
    # reprlib module has more than reprlib.repr() function
    # reprlib.Repr class implements the main functionality of reprlib
    # supports customization trough subclassing
    # http://docs.python.org/3/library/reprlib.html
