def lucas():
    """
    Generate numbers according to the Lucas (Star Wars) series
    :return: yield Lucas series number
    """
    yield 2
    a = 2
    b = 1
    while True:
        yield b
        a, b = b, a + b


generator = lucas()
for i in range(10):
    print(next(generator))


