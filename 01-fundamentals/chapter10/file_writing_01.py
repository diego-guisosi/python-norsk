# open file in write and text mode
f = open('wasteland.txt', mode='wt', encoding='utf-8')

# write() returns the amount of chars written to the file
print(f.write('What are the roots that clutch, '))
print(f.write('What branches grow\n'))
print(f.write('Out of this stony rubbish? '))

# the content will only be available in the file after close()
f.close()