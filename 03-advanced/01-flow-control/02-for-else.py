# else clause will be executed if the iterable is empty or after the handling of the last element of the serie


items = [2, 36, 25, 9]
# items = [2, 25, 9]  # uncomment this line to a different behavior
divisor = 12

for item in items:
    if item % divisor == 0:
        found = item
        break  # break will interrupt the loop without executing the "else" clause
else:  # nobreak
    items.append(divisor)
    found = divisor

print("{items} contains {found} which is a multiple of {divisor}".format(**locals()))