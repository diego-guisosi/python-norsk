# Applying an instance as a decorator calls the instance
# This kind of decorators are useful to create collections of decorated functions, which can dinamically be
# controlled


class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args, **kwargs)
        return wrap


tracer = Trace()


@tracer
def rotate_list(l):
    return l[1:] + [l[0]]


if __name__ == '__main__':
    l = [1, 2, 3]
    print(l)
    l = rotate_list(l)
    print(l)
    l = rotate_list(l)
    print(l)

    tracer.enabled = False
    l = rotate_list(l)
    print(l)
    l = rotate_list(l)
    print(l)
