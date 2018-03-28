''' Read and print an integer series. '''

import sys


# if the object implements context-manager protocol, it's possible to use with statement
# with statement open the resource, execute our block of code and closes the resource after completion
def read_series(filename):
    with open(filename, mode='rt', encoding='utf-8') as f:
        return [int(line.strip()) for line in f]


def main(filename):
    series = read_series(filename)
    print(series)


if __name__ == '__main__':
    main(sys.argv[1])