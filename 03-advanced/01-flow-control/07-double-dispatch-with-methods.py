# @functools.singledispatch dispatches based on the first argument. Since method's first argument always
# is self, single dispatch would always dispatch to the same type (the own object type)
# there is a way to reach the same behavior of singledispatch with methods tough. Take a look
from functools import singledispatch


class Shape:

    def __init__(self, solid):
        self.solid = solid


class Circle(Shape):

    def __init__(self, center, radius, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.center = center
        self.radius = radius

    def intersects(self, shape):
        # Delegate to the generic function, swapping arguments
        return intersects_with_circle(shape, self)  # switch the arguments so the functions receive first the type


class Parallelogram(Shape):

    def __init__(self, pa, pb, pc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pa = pa
        self.pb = pb
        self.pc = pc

    def intersects(self, shape):
        # Delegate to the generic function, swapping arguments
        return intersects_with_parallelogram(shape, self)


class Triangle(Shape):

    def __init__(self, pa, pb, pc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pa = pa
        self.pb = pb
        self.pc = pc

    def intersects(self, shape):
        # Delegate to the generic function, swapping arguments
        return intersects_with_triangle(shape, self)


@singledispatch
def intersects_with_circle(shape, circle):
    raise TypeError("Don't know how to compute intersection of {!r} with {!r}".format(circle, shape))


@intersects_with_circle.register(Circle)
def _(shape, circle):
    return circle_intersects_circle(circle, shape)


@intersects_with_circle.register(Parallelogram)
def _(shape, circle):
    return circle_intersects_parallelogram(circle, shape)


@intersects_with_circle.register(Triangle)
def _(shape, circle):
    return circle_intersects_triangle(circle, shape)


def circle_intersects_circle(circle, shape):
    print("circle_intersects_circle: {!r}, {!r}".format(circle, shape))


def circle_intersects_parallelogram(circle, shape):
    print("circle_intersects_parallelogram: {!r}, {!r}".format(circle, shape))


def circle_intersects_triangle(circle, shape):
    print("circle_intersects_triangle: {!r}, {!r}".format(circle, shape))


@singledispatch
def intersects_with_parallelogram(shape, parallelogram):
    raise TypeError("Don't know how to compute intersection of {!r} with {!r}".format(parallelogram, shape))


@intersects_with_parallelogram.register(Circle)
def _(shape, parallelogram):
    return parallelogram_intersects_circle(parallelogram, shape)


@intersects_with_parallelogram.register(Parallelogram)
def _(shape, parallelogram):
    return parallelogram_intersects_parallelogram(parallelogram, shape)


@intersects_with_parallelogram.register(Triangle)
def _(shape, parallelogram):
    return parallelogram_intersects_triangle(parallelogram, shape)


def parallelogram_intersects_circle(parallelogram, shape):
    print("parallelogram_intersects_circle: {!r}, {!r}".format(parallelogram, shape))


def parallelogram_intersects_parallelogram(parallelogram, shape):
    print("parallelogram_intersects_parallelogram: {!r}, {!r}".format(parallelogram, shape))


def parallelogram_intersects_triangle(parallelogram, shape):
    print("parallelogram_intersects_triangle: {!r}, {!r}".format(parallelogram, shape))


@singledispatch
def intersects_with_triangle(shape, triangle):
    raise TypeError("Don't know how to compute intersection of {!r} with {!r}".format(triangle, shape))


@intersects_with_triangle.register(Circle)
def _(shape, triangle):
    return triangle_intersects_circle(triangle, shape)


@intersects_with_triangle.register(Parallelogram)
def _(shape, triangle):
    return triangle_intersects_parallelogram(triangle, shape)


@intersects_with_triangle.register(Triangle)
def _(shape, triangle):
    return triangle_intersects_triangle(triangle, shape)


def triangle_intersects_circle(triangle, shape):
    print("triangle_intersects_circle: {!r}, {!r}".format(triangle, shape))


def triangle_intersects_parallelogram(triangle, shape):
    print("triangle_intersects_parallelogram: {!r}, {!r}".format(triangle, shape))


def triangle_intersects_triangle(triangle, shape):
    print("triangle_intersects_triangle: {!r}, {!r}".format(triangle, shape))


def main():
    shapes = [Circle(center=(0, 0), radius=5, solid=False),
              Parallelogram(pa=(0, 0), pb=(2, 0), pc=(1, 1), solid=False),
              Triangle(pa=(0, 0), pb=(1, 2), pc=(2, 0), solid=True)]

    shapes[0].intersects(shapes[1])
    shapes[1].intersects(shapes[0])


if __name__ == '__main__':
    main()