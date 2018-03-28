import time

message = 'global'


def enclosing():
    message = 'enclosing'

    def local():
        nonlocal message
        message = 'local'

    print('enclosing message', message)
    local()
    print('enclosing message', message)


# Sample usage of nonlocal.
def make_timer():
    """ Create a function whose result is the elapsed time between the created function calls"""
    last_called = None

    def elapsed():
        nonlocal last_called
        now = time.time()
        if last_called is None:
            last_called = now
            return None
        result = now - last_called
        last_called = now
        return result

    return elapsed


if __name__ == '__main__':
    print('global message', message)
    enclosing()
    print('global message', message)
    print()

    timer = make_timer()
    print(timer()) # Returns nothing, since it's the first call
    print(timer()) # Returns the elapsed time between the first and second call
    print(timer()) # Returns the elapsed time between the second and third call
