# generator comprehensions can be declared with parentheses
million_squares = (x*x for x in range(1, 1000001))

print(next(million_squares))
print(next(million_squares))

# to retrieve a new generator from the previous comprehension, it's necessary to declare it again
other_million_squares = (x*x for x in range(1, 1000001))

million_squares_sum = sum((x*x for x in range(1, 1000001)))
print(million_squares_sum)

# python let's us to omit comprehensions parentheses with functions that receives iterables
million_squares_sum = sum(x*x for x in range(1, 1000001))
print(million_squares_sum)
