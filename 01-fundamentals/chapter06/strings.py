import math

# Always use join to concatenate strings. + operator generate a new string to each concatenation
phrase  = "".join(("Diego ", "is ", "learning ", "python"))
phrase2 = "".join(["and ", "must ", "always ", "be ", "pythonic"])

print(phrase)
print(phrase2)
print()

csv = ",".join(["diego", "male", "29"])
print(csv)


formated = "Meu nome é {}. I'm {} years old".format("Diego", "29")

print
print(formated)

print("Meu nome é {name}. I'm {age} years old".format(age=29, name="Diego"))
print("Meu nome é {0}. I'm {1} years old. Yeah! {0} {1}. I promise".format("Diego", 29))


# It's possible to use an object with format
print()
print("pi={math.pi} e={math.e}".format(math=math))

# and also lists
numbers = [2, 5, 7]
print()
print("And that is the sequence: {num[0]}, {num[1]}, {num[2]}".format(num=numbers))

one = "one"
another_one = "one"
print(one is another_one)
# string are pooled like Java does
