# super()

# calling super() without arguments from within a method makes python provide the arguments

# within instance methods
#   super(class-of-method, self)
#
# doing so will return a proxy that resolve names right after the class-of-method in the MRO of the object. For
# single inheritance, this is the same of calling the method of the base class

# within class methods
#   super(class-of-method, class)
#
# the same as the previous description, but can only call directly static methods


# explicit examples

class A:
    def instance_method(self):
        return "A.instance"

    @classmethod
    def class_method(cls):
        return "A.class"


class B(A):
    def instance_method(self):
        return super().instance_method()
        # the same as super(B, self). The self instance method first param is passed as the second argument of super()

    @classmethod
    def class_method(cls):
        return super().class_method()
        # the same as super(B, cls). The cls class method first param is passed as the second argument of super()


b = B()
print(b.instance_method())
print(b.class_method())
