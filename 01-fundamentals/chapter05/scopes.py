# Demonstrates scopes

count = 0


def show_count():
    print("count = ", count)


def set_count(c):
    count = c
    print("count = ", count)


def set_global_count(c):
    global count
    count = c
    print("global count = ", count)


show_count()
set_count(100)
print(count)

set_global_count(200)
print(count)
