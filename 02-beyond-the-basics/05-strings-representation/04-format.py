# __format__ is called any time an object is used with string.format method
# it defaults to print __str__ implementation


class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '{point.x}, {point.y}'.format(point=self)

    def __repr__(self):
        return 'Point2D(x={}, y={})'.format(self.x, self.y)

    def __format__(self, format_spec):
        # the format_spec is the value provided after the collon in a format string field
        # e.g.: 'Formatted value: {:XYZ}'. If XYZ had been provided, format_spec would contain XYZ
        # if not provided, format_spec will be empty
        # In this example, we are defining a r (reverse) format. If provided, the order of x and y changes
        if format_spec == 'r':
            return '(({}, {}))'.format(self.y, self.x)
        else:
            return '(({}, {}))'.format(self.x, self.y)


if __name__ == '__main__':
    point = Point2D(x=10, y=20)
    print('{}'.format(point))
    print('{:r}'.format(point))
    print()

    # to force format to call __repr__ instead of __format__, we can use the !r in the formatting place holder
    print('{!r}'.format(point))

    # similarlly, we can bypass format to call __str__ implementation, using !s formatting place holder
    print('{!s}'.format(point))