class TestAssignmentContextManagement:

    def __enter__(self):
        return "You are in a with-block"

    def __exit__(self, exc_type, exc_val, exc_tb):
        return


class LoggingContextManager:

    def __enter__(self):
        print("LoggingContextManager.__enter__()")
        # Although we can return any value from __enter__() (including None), the most common implementation of this
        # method returns self (file is an example)
        return "You are in a with-block"

    def __exit__(self, exc_type, exc_val, exc_tb):
        # A common implementation to __exit__() is checking exc_type argument to determine if an exception has been
        # thrown by the with-block
        print("LoggingContextManager.__exit__({}, {}, {})".format(exc_type, exc_val, exc_tb))
        return


def main():

    with TestAssignmentContextManagement() as x:
        print(x)  # As we can see, the value returned by __enter__() is assigned to the variable after "as" keyword
    print()
    with LoggingContextManager() as x:
        print(x)
    print()
    with LoggingContextManager() as x:
        raise ValueError("Something has gone wrong!")
        print(x)


if __name__ == '__main__':
    main()