# unordered collection of unique elements
# set itself is mutable (itens can be added to it), but elements must be immutable
p = {6, 28, 496, 8128, 33550336}
print(p)
type(p)

d = {}  # curly braces make an empty dictionary
print(type(d))

e = set() # use set constructor to create an empty set
print(type(e))

# set constructor accepts any iterable
f = set([1, 9, 9, 10, 11, 11])
print(f)

# sets are iterable
for x in f:
    print(x)

print(9 in f)
print(12 not in f)

f.add(13)
f.add(9)  # elements that already exists are ignored
print(f)
print()

# updating sets with iterables
f.update([90, 92, 93, 93, 93])
print(f)

# removing elements
f.remove(93)
print(f)
try:
    f.remove(93)  # remove throws exception if element does not exist
except KeyError as e:
    print(e)
f.discard(93)
print(f)  # discard does not throw exception if the element is not present

# copying elements is possible with set constructor or copy function
shallow_copy = f.copy()
print(shallow_copy)

# sets with algebra
print()
print()
blue_eyes = {'Olivia', 'Harry', 'Lily', 'Jack', 'Amelia'}
blond_hair = {'Harry', 'Jack', 'Amelia', 'Mia', 'Joshua'}
smell_hcn = {'Harry', 'Amelia'}
taste_ptc = {'Harry', 'Lily', 'Amelia', 'Lola'}
o_blood = {'Mia', 'Joshua', 'Lily', 'Olivia'}
b_blood = {'Amelia', 'Jack'}
a_blood = {'Harry'}
ab_blood = {'Joshua', 'Lola'}

# people with blue eyes or blond hair
print(blue_eyes.union(blond_hair))
print(blue_eyes.union(blond_hair) == blond_hair.union(blue_eyes))  # commutative
print()

# people with blue eyes and blond_hair
print(blue_eyes.intersection(blond_hair))
print(blue_eyes.intersection(blond_hair) == blond_hair.intersection(blue_eyes))  # commutative
print()

# people with blond hair that doesn't have blue eyes
print(blond_hair.difference(blue_eyes))
print(blond_hair.difference(blue_eyes) == blue_eyes.difference(blond_hair))  # NOT commutative
print()

# people with blond hair that doesn't have blue eyes and people with blue eyes that doesn't have blond hair
# exclusive blond hair or blue eyes, but not both
print(blond_hair.symmetric_difference(blue_eyes))
print(blond_hair.symmetric_difference(blue_eyes) == blue_eyes.symmetric_difference(blond_hair))  # commutative
print()

# people who smell hcn also have blond hair
print(smell_hcn.issubset(blond_hair))
print(smell_hcn.issubset(blond_hair) == blond_hair.issubset(smell_hcn))  # NOT commutative
print()

# people who taste ptc also smell hcn
print(taste_ptc.issuperset(smell_hcn))
print(taste_ptc.issuperset(smell_hcn) == smell_hcn.issuperset(taste_ptc))  # NOT commutative
print()

# test if two sets have no members in common
# people with O blood type can not have A blood type and vice versa
print(o_blood.isdisjoint(a_blood))
print(a_blood.isdisjoint(o_blood) == o_blood.isdisjoint(a_blood))  # commutative