# Python allows static methods to be overwritten.

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

    # classmethod is often used to create factory methods to the class (as if it was a named constructor)
    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=None)

    @staticmethod
    def get_container_base_code():
        return "SC"

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._get_next_serial()
        self.base_code = self.get_container_base_code()  # if the class name had been used instead of self, the
                                                         # polymorphic behavior would not have happened
                                                         # examples on __main__


class RefrigeratedShippingContainer(ShippingContainer):

    @staticmethod
    def get_container_base_code():
        return "RSC"


if __name__ == '__main__':
    print(ShippingContainer.get_container_base_code())
    print(RefrigeratedShippingContainer.get_container_base_code())
    print()
    sc = ShippingContainer("ABC", None)
    rsc = RefrigeratedShippingContainer("DEF", None)
    print(sc.get_container_base_code())
    print(rsc.get_container_base_code())
