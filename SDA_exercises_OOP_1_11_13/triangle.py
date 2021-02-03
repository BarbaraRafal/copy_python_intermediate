from python_intermediate_training.SDA_exercises_OOP_1_11_13.figure import Figure


class Triangle(Figure):

    def __init__(self, a: float, h: float):
        self.a = a
        self.h = h

    def get_area(self):
        area = 1 / 2 * (self.a * self.h)
        return area
