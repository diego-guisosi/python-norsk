f= open('wasteland.txt', mode='at', encoding='utf-8')

# writelines() receives any iterable
f.writelines([
    'Son of man\n',
    'You cannot say, or guess, '
    'for you know only, \n'
    'A heap of broken images, '
    'where the sun beats\n'
])

f.close()