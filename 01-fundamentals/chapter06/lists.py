# lists indexing (or tuple indexing)
seq = "show how to index into sequences".split()

print(seq[0])
print(seq[5])
print(seq[-1])
print(seq[-6])

# lists or tuple slicing
print(seq[1:3])  # last index not included
print(seq[1:-1])  # all but first and last
print(seq[3:])  # from third to the end
print(seq[:3])  # from first to third
print(seq[:])  # the entire list... good sintax for copying a list
seq2 = seq[:]
print(seq2 is seq)  # it's not the same object
print(seq2 == seq)  # but the objects have the same values
print()

# other ways to copy lists
seq3 = seq.copy()
seq4 = list(seq)
print(seq3 is seq)
print(seq4 is seq)

# all these copies are shallow copies. The content is copied, but what is copied is the reference of each element
# of the list, not the values
