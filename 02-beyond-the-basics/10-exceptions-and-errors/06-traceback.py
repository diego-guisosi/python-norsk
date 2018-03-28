# Traceback contains all the function stack that raised the exception
import math
import sys
import traceback


class InclinationError(Exception):
    pass


def inclination(dx, dy):
    try:
        return math.degrees(math.atan(dy / dx))
    except ZeroDivisionError as e:
        # from keyword can be used to explicit assign an exception to another
        # Explicit chaining chains the exception to the __cause__ attribute
        raise InclinationError("Slope cannot be vertical") from e


def main():
    try:
        inclination(0, 5)
    except InclinationError as e:
        print("Traceback: ", e.__traceback__)

        # to interact with __traceback__, we must use traceback module
        traceback.print_tb(e.__traceback__)

        # traceback module is commonly used with logging functions
        # we can use traceback.format_tb instead of print_tb to return the a string with the traceback
        s = traceback.format_tb(e.__traceback__)
        print(s)

        # __traceback__ should always be used within the except block of the exception
        # never keep references to the traceback outside the scope of the except block
        # the size of traceback objects can be very large


if __name__ == '__main__':
    main()
    print("Finished")