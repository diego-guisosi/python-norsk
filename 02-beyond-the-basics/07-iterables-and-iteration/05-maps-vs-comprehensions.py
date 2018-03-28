# maps and comprehensions can produce the same results
# the which one to choose is up to you

i = (str(i) for i in range(5))
print(list(i))

i = map(str, range(5))
print(list(i))