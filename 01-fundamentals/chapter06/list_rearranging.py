# in place rearrangement of itens
g = [1, 11, 21, 1211, 112111]
g.reverse()
print(g)

d = [5, 17, 41, 29, 71, 149, 3299, 7, 13, 67]
d.sort()
print(d)

d.sort(reverse=True)
print(d)

h = "not perplexing do handwriting family where I illegibly know doctors".split()
h.sort(key=len)
print(' '.join(h))
print()

# to sort and not modify source list
e = sorted(d)  # sorted built-in function accepts the same parameters than sort() function
print(d)
print(e)
print()

# to reverse and not modify source list
h = reversed(g)
print(g)
print(h)  # different from sorted(), reversed built-in function returns an iterator
print(list(h))
