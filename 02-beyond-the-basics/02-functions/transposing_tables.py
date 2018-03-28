from pprint import pprint as pp

# transposing tables with zip

# zip combines two iterable per position

# day temperatures
sunday = [12, 14, 15, 15, 17, 21, 22, 23]
monday = [13, 14, 14, 14, 16, 20, 21, 22]

for item in zip(sunday, monday):
    print(item)

print()
daily = [sunday, monday]

for item in zip(*daily):
    print(item)

print()
transposed = list(zip(*daily))
pp(transposed)