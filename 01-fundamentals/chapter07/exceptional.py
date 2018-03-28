import sys

def convert(x):

    converted_int = -1
    try:
        converted_int = int(x)
        print("Conversion of {} succeed: {}".format(x, converted_int))
    except (ValueError, TypeError):
        print("Conversion of {} failed: {}".format(x, converted_int))
    return converted_int


def convert_2(x):

    converted_int = -1
    try:
        converted_int = int(x)
    except (ValueError, TypeError):
        pass  # if pass is not provided, python raises IdentationError, since empty blocks are not allowed in python
    return converted_int


def convert_3(x):

    try:
        return int(x)
    except (ValueError, TypeError) as e:
        print("Conversion error: {}".format(str(e)), file=sys.stderr)
        return -1


def convert_4(x):

    try:
        return int(x)
    except (ValueError, TypeError) as e:
        print("Conversion error: {}".format(str(e)), file=sys.stderr)
        raise  # exceptions must be raised. They should not pass silently
        # raise throws the exception being handled, if no parameter is provided
    finally:
        print("Closing resources")


convert("35")
convert("hedgehog")  # raises ValueError
convert([1, 2, 3])   # raises TypeError
print(convert_2("simplemind"))
print(convert_3("radiohead"))

print(convert_4("yep"))
