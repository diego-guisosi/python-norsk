tu = ("Diego", 15, 15.1)

for t in tu:
    print(t)


numbers = [5, 6, 9, 10, 1]

print(numbers[2])


def get_min_max(numbers):
    return min(numbers), max(numbers)


# tuple unpacking
a, b = get_min_max(numbers)


print(a, b)

a, b = b, a

print(a, b)