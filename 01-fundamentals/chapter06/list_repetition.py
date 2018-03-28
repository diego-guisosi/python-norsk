# when used with strings or lists, * works as a repetition operator
# it can be used to initialize lists with default values

my_list = [0] * 3
print(my_list)
print()

# with the repetition operator, the previous list was initiated with three elements containing the value zero

my_string = "Diego " * 4
print(my_string)
print()
# the same applies to strings


# repetition is shallow
other_list = [[-1, +1]] * 5
print(other_list)
print(other_list[0] is other_list[1])
other_list[3].append(7)
print(other_list)

print()
another_one = [[-1, +1] * 5]
print(another_one)
print(another_one[0][0] is another_one[0][3])

