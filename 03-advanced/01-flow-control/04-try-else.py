# else clause will be executed if no exception is raised
# this structure is used when we want to separate functions that can raise the same exception, because we are interested
# in handling only a specific one

try:
    f = open("example_file.txt", 'r')
except OSError:
    print("File could not be opened for read")
else:
    # Now we are sure the file is open
    print("Number of lines", sum(1 for line in f))
    f.close()
