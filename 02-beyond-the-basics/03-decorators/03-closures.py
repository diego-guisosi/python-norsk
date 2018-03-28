# python implements closures with the special attribute __closure__
# if the local function closed over an enclosing function attribute, the necessary references are kept by the
# __closure__ attribute of the local function


def enclosing():
    x = 'closed over'

    def local_func():
        print(x)
    return local_func


if __name__ == '__main__':
    local_func = enclosing()
    local_func()
    print(local_func.__closure__)