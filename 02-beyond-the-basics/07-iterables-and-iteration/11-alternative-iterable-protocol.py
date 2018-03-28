# An alternate protocol can be used instead of Iterable protocol
# __getitem__ must return an element, based on the index provided. If the index is out of range, must raise IndexError


class AlternateIterable:

    def __init__(self):
        self.data = [1, 2, 3]

    def __getitem__(self, idx):
        return self.data[idx]


for item in AlternateIterable():
    print(item)

print()
[print(item) for item in AlternateIterable()]