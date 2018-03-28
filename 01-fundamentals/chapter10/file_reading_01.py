f = open('wasteland.txt', mode='rt', encoding='utf-8')

# the parameter indicates the amount of chars (codepoints) to read
read32 = f.read(32)
print(read32)

# if no parameter is provided, the entire file is read.
# since this file was already read, the read() function will return the rest of the file
restRead = f.read()

# seek(0) points the file cursor back to the beginning
f.seek(0)

print(f.readline())
print(f.readline())
print(f.readline())  # if there is no more content to read, an empty string is returned

f.seek(0)

# reads all lines of the file and put it into a list (in the memory)
print(f.readlines())
f.close()