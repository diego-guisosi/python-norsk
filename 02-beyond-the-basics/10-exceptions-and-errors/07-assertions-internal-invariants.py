# Assertions are used test behaviors that should never happen with our program
# format: assert condition, optional_string


def modulus_three(n):
    r = n % 3
    if r == 0:
        print("Multiple of 3")
    elif r == 1:
        print("Remainder 1")
    else:  # r == 2
        print("Remainder 2")


# instead of using the comment above on the else statement, we could have use an assertion to document our assumption
def modulus_three_a(n):
    r = n % 3
    if r == 0:
        print("Multiple of 3")
    elif r == 1:
        print("Remainder 1")
    else:
        assert r == 2, "Remainder is not 2"
        print("Remainder 2")


def modulus_three_a(n):
    r = n % 4
    if r == 0:
        print("Multiple of 3")
    elif r == 1:
        print("Remainder 1")
    elif r == 2:
        print("Remainder 2")
    elif r == 3:
        print("Remainder 3")
    else:
        assert False, "This should never happen"


# Assertions should never be used to validate arguments of the function. Instead, they should validate the
# implementation of the functions