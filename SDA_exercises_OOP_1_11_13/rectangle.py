from python_intermediate_training.SDA_exercises_OOP_1_11_13.figure import Figure


class Rectangle(Figure):

    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def get_area(self):
        area = self.a * self.b
        return area
