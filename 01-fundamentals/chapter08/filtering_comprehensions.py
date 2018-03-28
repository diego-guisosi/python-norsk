from math import sqrt


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


# syntax -> expr(item) for item in iterable if predicate(item)
# note that the most simple expression for the comprehension can be the own item
primes = [x for x in range(101) if is_prime(x)]
print(primes)

even_pows = {x: x*x for x in range(20) if x % 2 == 0}
print(even_pows)
odd_pows = {x: x*x for x in range(20) if x % 2 != 0}
print(odd_pows)