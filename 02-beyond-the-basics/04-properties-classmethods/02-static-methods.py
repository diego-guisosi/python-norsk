class ShippingContainer:

    next_serial = 1337

    # this decorator can be used to create static methods
    @staticmethod
    def _get_next_serial():
        next_number = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return next_number

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._get_next_serial()


if __name__ == '__main__':
    c1 = ShippingContainer("ESC", "eletronics")
    c2 = ShippingContainer("ESC", "pharmaceuticals")

    print(c1.serial)
    print(c2.serial)
    print(ShippingContainer.next_serial)
    print(c1.next_serial)