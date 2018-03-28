# python objects
class Car:

    def __init__(self, model, color):
        self.model = model
        self.color = color

    def __str__(self):
        return "Model: {self.model} - Color: {self.color}".format(self=self)

    def get_model(self):
        return self.color

    def get_color(self):
        return self.color


class Ferrari(Car):

    def __init__(self, color):
        super().__init__("Ferrari", color)


car = Car(model="208", color="White")
print(car)

ferrari = Ferrari(color="Red")
print(ferrari)