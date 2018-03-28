# a common use for closures are function factories


def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp


if __name__ == '__main__':
    square = raise_to(2)
    print(square.__closure__)
    print(square(2))
    print()

    cube = raise_to(3)
    print(cube.__closure__)
    print(cube(2))
