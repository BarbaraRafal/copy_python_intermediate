from math import pi
from python_intermediate_training.SDA_exercises_OOP_1_11_13.figure import Figure


class Circle(Figure):

    def __init__(self, r: float):
        self.r = r

    def get_area(self):
        area = pi * self.r * self.r
        return round(area, 2)
