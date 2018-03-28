w = "the quick brown fox jumps over the lazy dog".split()
print(w)

index = w.index('fox')
print(index)
print(w[index])
try:
    index = w.index('unicorn')
    print(index)
except ValueError as e:
    print(e)

# counting elements
print(w.count('the'))
print(w.count("unicorn"))
print()
print("fox" in w)
print("pig" in w)
print()

# del removes elements by index
del w[1]
print(w)

# list.remove() removes by content, which is a shorthand to del list[list.index("content")]
w.remove("brown")
print(w)
try:
    w.remove("unicorn")
except ValueError as e:
    print(e)
print()

# it's also possible to insert elements into specific positions, repositioning other elements if necessary
w.insert(1, "quick")
print(w)

back_to_the_string = " ".join(w)
print(back_to_the_string)