# comprehensions can have multiple inputs and if clauses

l = [(x,y) for x in range(5) for y in range(3)]
print(l)

# the comprehension below represents the following looping structure
l = []
for x in range(5):
    for y in range(3):
        l.append((x,y))

print(l)

# the last statement can refer to earlier statement clauses
values = [
    x / (x - y)
    for x in range(100)
    if x > 50
    for y in range(100)
    if x - y != 0  # this statement if refering to x from the earlier statement
]
print(values)

# last comprehension interpreted as a loop
values = []
for x in range(100):
    if x > 50:
        for y in range(100):
            if x - y != 0:
                values.append(x / (x - y))
print(values)

# the second statement is referencing the first statement x variable
coordinates = [(x, y) for x in range(10) for y in range(x)]
print(coordinates)

# loop representing the previous comprehension
coordinates = []
for x in range(10):
    for y in range(x):
        coordinates.append((x, y))
print(coordinates)