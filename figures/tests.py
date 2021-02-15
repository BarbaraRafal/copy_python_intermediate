import pytest
from python_intermediate_training.figures.figures_entities import Circle
from python_intermediate_training.figures.figures_entities import Triangle
from python_intermediate_training.figures.figures_entities import Rectangle
from python_intermediate_training.figures.figures_entities import Figure


def test_count_area():
    #  given
    circle1 = Circle(1)
    triangle1 = Triangle(2, 1)
    rectangle1 = Rectangle(2, 2)

    #  when
    result = Figure.count_area([circle1, triangle1, rectangle1])
    #  then
    assert result == 8.14

def test_get_area():

    #  given
    circle1 = Circle(1)
    triangle1 = Triangle(2, 1)
    rectangle1 = Rectangle(2, 2)


    #  when
    figure_area_1 = Circle.get_area(circle1)
    figure_area_2 = Triangle.get_area(triangle1)
    figure_area_3 = Rectangle.get_area(rectangle1)

    # then

    assert figure_area_1 == 3.14
    assert figure_area_2 == 1
    assert figure_area_3 == 4
