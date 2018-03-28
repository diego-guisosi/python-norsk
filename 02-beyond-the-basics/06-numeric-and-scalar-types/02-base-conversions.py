b = 0b101010
o = 0o52
x = 0x2a

print(b, o, x)
print()
print(bin(42))
print(oct(42))
print(hex(42))
print()
# it is possible to use string slicing to remove the prefix base notation
print(hex(42)[2:])
print()
# uses 0-9 and a-z for digits in bases from 2 to 36 on int constructor
print(int('2a', base=16))
print(int('acghd', base=18))
print(int('0b111000', base=2))
# base=0 is the same as decimal
print(int('0o664', base=0))

# No support for base 1 (tallying)
