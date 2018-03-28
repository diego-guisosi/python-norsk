# loca functions can be returned from enclosing functions

def enclosing():
    def local_function():
        print('local function')
    return local_function


if __name__ == '__main__':
    local_func = enclosing()
    local_func()