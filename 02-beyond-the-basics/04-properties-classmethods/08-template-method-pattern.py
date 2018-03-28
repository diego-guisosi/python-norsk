# Using template method pattern to avoid the use of fset


class ShippingContainer:

    HEIGHT_FT = 8.5
    WIDTH_FT = 8.0

    next_serial = 1337

    @classmethod
    def _get_next_serial(cls):
        next_number = cls.next_serial
        cls.next_serial += 1
        return next_number

    @classmethod
    def create_empty(cls, owner_code, length_ft, *args, **kwargs):
        return cls(owner_code, length_ft, contents=None, *args, **kwargs)

    @staticmethod
    def get_container_base_code():
        return "SC"

    def __init__(self, owner_code, length_ft, contents):
        self.owner_code = owner_code
        self.length_ft = length_ft
        self.contents = contents
        self.serial = ShippingContainer._get_next_serial()
        self.base_code = self.get_container_base_code()

    def _extract_volume(self):
        return ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self.length_ft

    @property
    def volume_ft3(self):
        return self._extract_volume()



class RefrigeratedShippingContainer(ShippingContainer):

    MAX_CELSIUS = 4.0
    FRIDGE_VOLUME_FT3 = 100

    @staticmethod
    def get_container_base_code():
        return "RSC"

    @staticmethod
    def _c_to_f(celsius):
        return celsius * 9/5 + 32

    @staticmethod
    def _f_to_c(fahrenheit):
        return (fahrenheit - 32) *5/9

    def __init__(self, owner_code, length_ft, contents, celsius):
        super().__init__(owner_code, length_ft, contents)
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    def _set_celsius(self, value):
        if value > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature too hot!")
        self._celsius = value

    @celsius.setter
    def celsius(self, value):
        self._set_celsius(value)

    @property
    def readonly_class(self):
        return self.__class__

    @property
    def fahrenheit(self):
        return RefrigeratedShippingContainer._c_to_f(self.celsius)  # Accessing the property instead of _celsius

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = RefrigeratedShippingContainer._f_to_c(value)

    # @property was removed, because with the template method is only necessary to overwrite _extract_volume method
    def _extract_volume(self):
        return super()._extract_volume() - RefrigeratedShippingContainer.FRIDGE_VOLUME_FT3


class HeatedRefrigeratedShippingContainer(RefrigeratedShippingContainer):

    MIN_CELSIUS = -20.0

    def _set_celsius(self, value):
        if value < HeatedRefrigeratedShippingContainer.MIN_CELSIUS:
            raise ValueError("Temperature too cold!")
        super()._set_celsius(value)


if __name__ == '__main__':
    hrsc = HeatedRefrigeratedShippingContainer.create_empty("DEF", celsius=-18.0, length_ft=40)
    print(hrsc.volume_ft3)
    hrsc.celsius = -21.0
