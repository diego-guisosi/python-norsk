# Multiple context managers can be used with with-statements
# Use:
#   with cm1() as a, cm2() as b:
#       BODY
# Equivalence:
#   with cm1() as a:
#       with cm2() as b:
#           BODY
# Exception handling:
#   Exceptions propagated from inner context managers will be seen by outer context manager
#   If inner context manager swallows the exception, the outer context manager will not receive the exception

import contextlib


@contextlib.contextmanager
def nest_test(name, propagate=False):
    try:
        print('Entering ', name)
        yield name
        print('Exiting {} normally'.format(name))
    except Exception:
        print('{} Received an exception!'.format(name))
        if propagate:
            raise


def main():
    # Inner context managers can reference outer context manager "as VAR" references
    with nest_test('outer') as n1, nest_test('inner, nested in ' + n1):
        print("BODY")

    # The above structure is a shorthand to the structure below:
    print()

    with nest_test('outer'):
        with nest_test('inner'):
            print("BODY")

    print()
    with nest_test('outer', propagate=True) as n1, nest_test('inner', propagate=False):
        print("BODY")
        raise ValueError("Something has been wrong")

    print()
    with nest_test('outer', propagate=False) as n1, nest_test('inner', propagate=True):
        print("BODY")
        raise ValueError("Something has been wrong")

    print()
    with nest_test('outer', propagate=True) as n1, nest_test('inner', propagate=True):
        print("BODY")
        raise ValueError("Something has been wrong")


if __name__ == '__main__':
    main()