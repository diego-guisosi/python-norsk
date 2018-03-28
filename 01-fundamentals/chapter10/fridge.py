''' Demonstrate raiding a refrigerator '''
from contextlib import closing


class RefrigeratorRaider:
    ''' Raid a refrigerator '''

    def open(self):
        print("Open fridge door.")

    def take(self, food):
        print("Finding {}...".format(food))
        if food == 'deep fried pizza':
            raise RuntimeError("Health Warning!")
        print("Taking {}".format(food))

    def close(self):
        print("Close fridge door.")


def raid(food):
    r = RefrigeratorRaider()
    r.open()
    r.take(food)
    r.close()


def raidAutoClose(food):
    with closing(RefrigeratorRaider()) as r:
        r.open()
        r.take(food)


raid("Milk")

try:
    raid('deep fried pizza')  # this will raise an exception that will prevent RefrigeratorRaider to close
except RuntimeError as e:
    print(str(e))

raidAutoClose('deep fried pizza')  # even though the exception is raised, close is called by contextlib.closing