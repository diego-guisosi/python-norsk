def main():
    print(SystemExit.mro())
    print(KeyboardInterrupt.mro())
    print(ValueError.mro())
    print(IndexError.__mro__)
    print(KeyError.mro())
    print(FileNotFoundError.mro())
    print(PermissionError.__mro__)


if __name__ == '__main__':
    main()

# BaseException is the base class of all exceptions
# if a base class exception is handled by an except block, all subclasses of that exception will be handled
