# calling print passing an object as argument will call str implementation
# calling print passing a built-in type (such as collections) will call repr implementation of the objects


class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '{point.x}, {point.y}'.format(point=self)

    def __repr__(self):
        return 'Point2D(x={}, y={})'.format(self.x, self.y)


if __name__ == '__main__':
    point = Point2D(x=10, y=20)
    print('The circle is centered at ({})'.format(point))
    print([Point2D(x=i, y=i*2) for i in range(3)])
    print({i: Point2D(x=i, y=i * 2) for i in range(3)})

    set_str = str({Point2D(x=i, y=i * 2) for i in range(3)})
    print(set_str)
    