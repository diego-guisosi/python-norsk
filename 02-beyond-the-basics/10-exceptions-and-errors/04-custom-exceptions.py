import math


# Always inherit from Exception to create custom exceptions
class TriangleError(Exception):
    # Since TriangleError does not have body, all the functionality will be inherited from Exception which,
    # in that case, it will be:
    # __init__, __str__ and __repr__
    pass


class DetailedTriangleError(Exception):

    def __init__(self, text, sides):
        super().__init__(text)
        self._sides = tuple(sides)

    @property
    def sides(self):
        return self._sides

    def __str__(self):
        return "'{}' for sides '{}'".format(self.args[0], self._sides)

    def __repr__(self):
        return "DetailedTriangleError({!r}, {!r})".format(self.args[0], self._sides)


def triangle_area(a, b, c):
    sides = sorted((a, b, c))
    if sides[2] > sides[0] + sides[1]:
        raise TriangleError("Illegal triangle")
    if sides[2] == 5:
        raise DetailedTriangleError("Illegal triangle", sides)
    p = (a + b + c) / 2
    a = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return a


def main():
    try:
        triangle_area(3, 4, 10)
    except TriangleError as e:
        print("Payload: ", e.args)

    triangle_area(3, 4, 5)


if __name__ == '__main__':
    main()