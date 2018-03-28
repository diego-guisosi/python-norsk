if __name__ == '__main__':
    # ascii replaces non ascii chars with espace sequences
    hello = 'Olá'
    print(ascii(hello))
    print()
    #
    # ord and chr are complementary functions and each reverts the other
    # ord converts a single character to its integer Unicode codepoint
    a = '¾'
    ord_a = ord(a)
    chr_a = chr(ord_a)
    print(ord_a)
    print(chr_a)
    print(ord(chr(190)))
    print(chr(ord(a)))

