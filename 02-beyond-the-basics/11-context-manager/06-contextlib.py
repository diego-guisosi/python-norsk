# This module provides helpers to facilitate the use and creation of context managers
# One example is the contextmanager decorator. We can decorate generators to act as factories of context managers
# The implementation must follow the pattern below:
#
# @contextlib.contextmanager
# def my_context_manager():
#   # <ENTER>                -> Here we implement what __enter__ should initialize
#   try:
#       yield [value]        -> This is equivalent to the end of __enter__. [value] will be returned to with-statement
#       # <NORMAL EXIT>      -> After with-block execution, this generator resumes from here to handle normal clean up.
#   except:
#       # <EXCEPTIONAL EXIT> -> If an exception is thrown in the with-block, this block of code will be executed
#       raise                -> Use standard exception handling to propagate exceptions
#                               Explicitly re-raise - or don't catch - to propagate exceptions
#                               Swallow exceptions by not re-raising them
# with my_context_manager() as x:
# . . .

import contextlib
import sys


@contextlib.contextmanager
def logging_context_manager():
    print("logging_context_manager: enter")
    try:
        yield "You are in a with block"
        print("logging_context_manager: normal exit")
    except Exception:
        print("logging_context_manager: exceptional exit", sys.exc_info())
        # declare "raise" here to propagate the exception


def main():
    with logging_context_manager() as x:
        print(x)
    print()
    with logging_context_manager() as x:
        print(x)
        raise ValueError("Execution Interrupted")


if __name__ == '__main__':
    main()