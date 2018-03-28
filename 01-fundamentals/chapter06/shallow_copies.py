# list copies are shallow. A new list containing the same object references of the source list is create.

my_list = [1, 2]
print(my_list)

my_copy = my_list[:]
print(my_copy)
print(my_copy is my_list)
print(my_copy == my_list)

my_other_list = [[1, 2], [3, 4]]
my_other_copy = my_other_list[:]
print(my_other_copy)
print(my_other_copy is my_other_list)
print(my_other_copy[0] is my_other_list[0])

# since the elements of my_other_list are references to other lists, the copied list contains the same references
# of my_other_list

my_other_list[1].append(5)
print(my_other_list[1])
print(my_other_copy[1])