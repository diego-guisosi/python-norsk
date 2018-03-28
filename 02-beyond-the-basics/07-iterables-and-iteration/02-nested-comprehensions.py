# comprehensions can be nested, so that a comprehension produces another comprehension

vals = [[y * 3 for y in range(x)] for x in range(10)]
print(vals)

# this comprehension can be expanded as follows
vals = []
for x in range(10):
    inner_vals = []
    for y in range(x):
        inner_vals.append(y * 3)
    vals.append(inner_vals)
print(vals)

# multi-input and nested comprehensions applies to any type of comprehension
# for instance: the set comprehension below creates a set containing the product of all numbers between 0-9
print({x * y for x in range(10) for y in range(10)})