# although loop-else structures are available, they are a little bit obscure and should be avoided
# we can achieve the same behavior of the for-else loop of 02-for-else.py with the following refactoring:


def ensure_has_divisible(items, divisor):
    for item in items:
        if item % divisor == 0:
            return item
        items.append(divisor)
        return divisor


items = [2, 36, 25, 9]
divisor = 12

dividend = ensure_has_divisible(items, divisor)
print("{items} contains {dividend} which is a multiple of {divisor}".format(**locals()))