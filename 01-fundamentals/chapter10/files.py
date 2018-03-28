import sys


def main(filename):
    file = open(filename, mode='rt', encoding='utf-8')
    for line in file:
        sys.stdout.write(line)  # this function writes without new line
    file.close()


if __name__ == '__main__':
    main(sys.argv[1])
