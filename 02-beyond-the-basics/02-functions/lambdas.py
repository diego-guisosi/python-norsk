# lambdas are annonymous callables

scientists = [
    'Marie Curie', 'Albert Einstein', 'Niels Bohr', 'Isaac Newton', 'Dmitri Mendelev', 'Antoine Lavoisier',
    'Carl Linnaeus', 'Alfred Wegener', 'Charles Darwin'
]

sorted_scientists = sorted(scientists, key=lambda name: name.split()[-1])
print(sorted_scientists)

# lambda below does not have argument
add_diego = lambda: scientists.append('Diego Guimaraes')

add_diego()
print(scientists)

# python lambdas can have only one expression
# arguments are separated with commas

print(callable(add_diego))