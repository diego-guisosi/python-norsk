# multiple decorators can be used with the same function
# they are applied on the reverse order
# in this example, escape_unicode will be first applied to norwegian_island_maker, which will return a new
# callable. This callable will then be passed to the other decorator (tracer).


def escape_unicode(f):
    def wrap(*args,**kwargs):
        x = f(*args, **kwargs)
        return ascii(x)

    return wrap


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
@escape_unicode
def norwegian_island_maker(name):
    return name + 'ói'


if __name__ == '__main__':
    print(norwegian_island_maker('Llama'))
    print(norwegian_island_maker('Python'))
    print(norwegian_island_maker('Troll'))