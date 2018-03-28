# Implicit chaining: when an exception occurs during the handling of another exception
# Explicit chaining: occurs when we deliberately assign an exception to another one on the except block
import math
import sys


class InclinationError(Exception):
    pass


def inclination(dx, dy):
    try:
        return math.degrees(math.atan(dy / dx))
    except ZeroDivisionError as e:
        # from keyword can be used to explicit assign an exception to another
        # Explicit chaining chains the exception to the __cause__ attribute
        raise InclinationError("Slope cannot be vertical") from e


class TriangleError(Exception):

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
        raise TriangleError("Illegal triangle", sides)
    p = (a + b + c) / 2
    a = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return a


def main():
    try:
        inclination(0, 5)
    except InclinationError as e:
        print("Payload: ", e.args)
        print("Payload context: ", e.__cause__.args)

    try:
        triangle_area(3, 4, 10)
    except TriangleError as e:
        # The statement below will raise an UnsupportedOperation, because of the attempt of printing the exception on
        # stdin instead of stderr
        # Implicit chaining chains the exception to the __context__ attribute
        print(e, file=sys.stdin)


if __name__ == '__main__':
    main()