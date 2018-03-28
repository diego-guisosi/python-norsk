# decorators can also be applied to methods


def escape_unicode(f):
    def wrap(*args,**kwargs):
        x = f(*args, **kwargs)
        return ascii(x)

    return wrap


class IslandMaker:
    def __init__(self, suffix):
        self.suffix = suffix

    @escape_unicode
    def make_island(self, name):
        return "{} {}".format(name, self.suffix)


if __name__ == '__main__':
    im = IslandMaker('Island')
    print(im.make_island("Python"))