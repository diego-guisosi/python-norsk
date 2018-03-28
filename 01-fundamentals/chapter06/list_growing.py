m = [1, 2, 3]
n = [4, 5]

# + operator results in a new list without modification of the operands
# m and n are kept with the same values and the new list is assigned to k
k = m + n
print(k)

# += modifies the assignee in place
# k is modified, referencing the new list created
k += [5, 6, 7, 8]
print(k)

# the same behavior of += can be achieved with extend()
k.extend([10, 11])
print(k)

# the operations above apply to any iterable
