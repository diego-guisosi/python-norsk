# Class methods also behaves polymorphic, so that the class reference passed to cls parameter represent the actual
# class of the instance
# This way, factory methods can instantiate polymorphic the correct instance

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
    def create_empty(cls, owner_code, *args, **kwargs):         # args and kwargs have been added to make it possible to
        return cls(owner_code, contents=None, *args, **kwargs)  # accept the additional argument of the
                                                                # RefrigeratedShippingContainer

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

    MAX_CELSIUS = 4.0

    @staticmethod
    def get_container_base_code():
        return "RSC"

    def __init__(self, owner_code, contents, celsius):
        super().__init__(owner_code, contents)
        if celsius > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature too hot!")
        self.celsius = celsius


if __name__ == '__main__':
    sc = ShippingContainer.create_empty("ABC")
    rsc = RefrigeratedShippingContainer.create_empty("DEF", celsius=3)
    print(type(sc) is ShippingContainer)
    print(type(sc) is RefrigeratedShippingContainer)
    print(type(rsc) is ShippingContainer)
    print(type(rsc) is RefrigeratedShippingContainer)

    rsc3 = RefrigeratedShippingContainer.create_empty("ABC", celsius=3.0)
    RefrigeratedShippingContainer.create_empty("ABC", celsius=5.0)

    # Since create_empty classmethod receives the correct class as cls parameter,
    # the additional argument celsius can be passed to RefrigeratedShippingContainer constructor
    