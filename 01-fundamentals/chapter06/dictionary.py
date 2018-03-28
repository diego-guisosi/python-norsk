from pprint import pprint as pp

# it's an unordered map
names_and_ages = [("Alice", 32), ("Bob", 48), ("Charlie", 28), ("Daniel", 33)]
d = dict(names_and_ages)
print(d)
print()

phonetic = dict(a="alfa", b="beta", c="charlie", d="delta", e="echo")
print(phonetic)

# copying dictionaries
d = dict(goldenrod=0xDAA520, indigo=0x4B0082, seashell=0xFFF5EE)
print(d)
e = d.copy()
print(e)
f = dict(e)
print(f)
print()

# updating a dictionary
g = dict(wheat=0xF5DEB3, khaki=0xF0E68C, crimson=0xDC143C)
f.update(g)
print(f)

# updating with dictionary containing pre-existing key
h = dict(wheat=0x000000)
f.update(h)
print(f)
print()

# dictionaries are iterables
for key in f:
    print("{key}: {value}".format(key=key, value=f[key]))
print()

for key in f.keys():
    print(key)
print()

for value in f.values():
    print(value)
print()

for key, value in f.items():  # tuple containing items (key + value) of the dictionary
    print("{key} => {value}".format(key=key, value=value))
print()

print("wheat" in f)
print("blue" not in f)

# del can be used to remove items by key
del f['wheat']
print(f)
try:
    del f['blue']
    # exception is thrown when the key is not found to delete
except KeyError as e:
    print(e)


# dictionary itself is mutable (itens can be added). Keys are imutable and values are mutable
m = {'H': [1, 2, 3],
     'He': [3, 4],
     'Li': [6, 7],
     'Be': [7, 9, 10],
     'B': [10, 11],
     'C': [11, 12, 13, 14]}
m['H'] += [4, 5, 6, 7]
print(m)
m['N'] = [13, 14, 15]
print(m)
print()

print("Pretty Print")
pp(m)