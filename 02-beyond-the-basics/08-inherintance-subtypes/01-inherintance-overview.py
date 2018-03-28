class Base:

    def __init__(self):
        print("Base initialized")

    def f(self):
        print("Base.f()")


class Sub01(Base):
    pass


class Sub02(Base):

    # Overwrite
    def f(self):
        print("Sub02.f()")


class Sub03(Base):

    def __init__(self):
        print("Sub03 initialized")


class Sub04(Base):

    def __init__(self):
        super().__init__()
        print("Sub04 initialized")


base= Base()
base.f()
print()
# since Sub01 __init__ was not defined, by default, the Base __init__ is called
sub_01 = Sub01()
sub_01.f()
print()
sub_02 = Sub02()
sub_02.f()
print()
# since __init__ was implemented on Sub03, Base __init__ is not called. To do so, we must explicit call super().__init
sub_03 = Sub03()
sub_03.f()
print()
sub_04 = Sub04()
sub_04.f()