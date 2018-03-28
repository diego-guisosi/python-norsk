class ShippingContainer:

    next_serial = 1337

    # this decorator works very alike staticmethod. The difference is that this decorator passes the class to the
    # method, which can be used the same way we use self to access instance variables, but the variable will give
    # access to class variables
    # by default, the name of the parameter to which the class will be assigned is 'cls'
    # prefer to use classmethod when it's necessary to access class variables and staticmethod when it's not
    @classmethod
    def _get_next_serial(cls):
        next_number = cls.next_serial
        cls.next_serial += 1
        return next_number

    # classmethod is often used to create factory methods to the class (also known as named constructors)
    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=None)

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._get_next_serial()


if __name__ == '__main__':
    c1 = ShippingContainer("ESC", "eletronics")
    c2 = ShippingContainer("ESC", "pharmaceuticals")
    c3 = ShippingContainer.create_empty('ESC')

    print(c1.serial)
    print(c2.serial)
    print(c3.serial)
    print(c3.owner_code)
    print(c3.contents)
    print(ShippingContainer.next_serial)
    print(c1.next_serial)
