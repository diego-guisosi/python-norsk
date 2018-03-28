class ShippingContainer:

    # the variable below is a class variable. This variable will be shared among all instances of the class
    # since classes don't declare a new scope, this variable cannot be directly accessed. It is necessary to
    # provide the class name, as shown in __init__
    # Python scopes aew
    #   L, Local
    #   E, Enclosing
    #   G, Global
    #   B, Built-in (e.g.: open, range, SyntaxError
    next_serial = 1337

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer.next_serial  # we could have used self.next_serial to access the class attribute
                                                     # since all instances share the same class atrribute,
                                                     # but using the class name is more explicit

        ShippingContainer.next_serial += 1           # here we can not use self.next_serial to assign values to the
                                                     # class attribute. Doing so will create an instance attribute
                                                     # named next_serial, that will shadow the class attribute



if __name__ == '__main__':
    c1 = ShippingContainer("ESC", "eletronics")
    c2 = ShippingContainer("ESC", "pharmaceuticals")

    print(c1.serial)
    print(c2.serial)
    print(ShippingContainer.next_serial)
    print(c1.next_serial)