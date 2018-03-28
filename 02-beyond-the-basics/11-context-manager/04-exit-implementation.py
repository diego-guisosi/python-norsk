class LoggingContextManager:

    def __enter__(self):
        print('LoggingContextManager.__enter__()')
        return 'You are in a with-block!'

    # By default, __exit__ propagates exceptions thrown from the with-statement's code block
    # This can be controlled based on the return value of __exit__
    # If True is returned, the exception is swallowed. If False, the exception is propagated
    # The __exit__ below does not return any value. By default, functions return None. Since None evaluate to False,
    # the exception is being propagated
    # IMPORTANT: __exit__ should never explicitly re-raise an exception. If the exception must be raised, return False
    #            __exit__ should only raise exceptions if it fails itself
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print('LoggingContextManager.__exit__(): Normal exit detected')
        else:
            print('LoggingContextManager.__exit__():'
                  'Exception detected!'
                  'type={}, value={}, traceback={}'.format(
                exc_type, exc_val, exc_tb
            ))


def main():
    with LoggingContextManager() as x:
        print(x)

    try:
        with LoggingContextManager() as x:
            raise ValueError("Problem happened during execution")
    except ValueError:
        print("*** ValueError detected ***")


if __name__ == '__main__':
    main()