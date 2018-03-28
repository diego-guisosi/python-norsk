import reader.reader
import sys

r = reader.Reader(sys.argv[1])
try:
    print(r.read())
finally:
    r.close()
