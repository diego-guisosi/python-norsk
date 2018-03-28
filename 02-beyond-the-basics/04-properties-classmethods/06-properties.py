# Properties can be created to prevent direct modification of attributes
# e.g.: The celsius instance attribute can be reassigned by the RefrigeratedShippingContainer constructor caller


class ShippingContainer:
    next_serial = 1337

    @classmethod
    def _get_next_serial(cls):
        next_number = cls.next_serial
        cls.next_serial += 1
        return next_number

    @classmethod
    def create_empty(cls, owner_code, *args, **kwargs):
        return cls(owner_code, contents=None, *args, **kwargs)

    @staticmethod
    def get_container_base_code():
        return "SC"

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._get_next_serial()
        self.base_code = self.get_container_base_code()


class RefrigeratedShippingContainer(ShippingContainer):
    MAX_CELSIUS = 4.0

    @staticmethod
    def get_container_base_code():
        return "RSC"

    # since the two methods below does not depend on the instance of the class and the are not generally enough
    # to be outside the class, they are good candidates to static methods
    @staticmethod
    def _c_to_f(celsius):
        return celsius * 9/5 + 32

    @staticmethod
    def _f_to_c(fahrenheit):
        return (fahrenheit - 32) *5/9

    def __init__(self, owner_code, contents, celsius):
        super().__init__(owner_code, contents)
        #self._celsius = celsius  # with the _, we indicate that the attribute should not be used outside the class
        self.celsius = celsius  # celsius property is being used here to take advantage of the setter validation
                                # so that is not necessary to repeat the logic here

    # the decorator bellow will create a property object and bind it to the celsius method name
    # this property object can be accessed like this "rsc.celsius" and does not allow celsius assignment by the caller
    @property
    def celsius(self):
        return self._celsius

    # the property object created by the property decorator provides another decorators that can be used to modify
    # the property object. The decorator bellow modifies the property object, adding to it setter capabilities
    @celsius.setter
    def celsius(self, value):
        if value > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature too hot!")
        self._celsius = value

    @property
    def readonly_class(self):
        return self.__class__

    @property
    def fahrenheit(self):
        return RefrigeratedShippingContainer._c_to_f(self.celsius)  # Accessing the property instead of _celsius

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = RefrigeratedShippingContainer._f_to_c(value)
        # Since the assingment is trying to modify the celsius property instead of directly modify _celsius,
        # the celsius setter temperature validation is being executed


if __name__ == '__main__':
    rsc = RefrigeratedShippingContainer.create_empty("ABC", celsius=2.0)
    print(rsc.celsius)
    rsc.celsius = 3.0
    print(rsc.celsius)
    try:
        rsc.celsius = 4.0
    except ValueError as e:
        print(str(e))
    print()
    print(rsc.readonly_class)

    # Since we don't have a setter to readonly_class property, python runtime prevents the assignment
    try:
        rsc.readonly_class = "XPTO"
    except AttributeError as e:
        print(str(e))

    print()
    print(rsc.fahrenheit)
    rsc.fahrenheit = 23
    print(rsc.fahrenheit)
    print(rsc.celsius)