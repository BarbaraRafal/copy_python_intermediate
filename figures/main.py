from python_intermediate_training.figures.figures_entities import *


def main():
    circle1 = Circle(1)
    circle2 = Circle(10)
    circle3 = Circle(15)
    triangle1 = Triangle(2, 1)
    triangle2 = Triangle(20, 10)
    triangle3 = Triangle(10, 5)
    rectangle1 = Rectangle(2, 2)
    rectangle2 = Rectangle(45, 5)
    rectangle3 = Rectangle(50, 5)

    print(circle1.get_area())
    print(triangle1.get_area())
    print(rectangle1.get_area())

    area = Figure.count_area([triangle3, circle3, rectangle2])
    print(area)


if __name__ == "__main__":
    main()
