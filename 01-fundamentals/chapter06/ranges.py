sequence1 = range(5)
sequence2 = range(5, 10)
sequence3 = range(0, 10, 2)


print([str(seq) for seq in sequence1])
print([str(seq) for seq in sequence2])
print([str(seq) for seq in sequence3])


for i in range(3):
    print("Jam")

# do NOT use range to iterate collections. Prefer direct use of for with the collection after "in
my_list = [1, 2, 3]
for i in range(len(my_list)): # this is NOT pythonic
    print(my_list[i])

for item in my_list:
    print(item) # this IS

for index, item in enumerate(my_list):
    print("{}: {}".format(index, item)) # and this IS too, if you need a counter or an index