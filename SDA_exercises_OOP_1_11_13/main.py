from python_intermediate_training.SDA_exercises_OOP_1_11_13.circle import Circle
from python_intermediate_training.SDA_exercises_OOP_1_11_13.triangle import Triangle
from python_intermediate_training.SDA_exercises_OOP_1_11_13.rectangle import Rectangle


# ponizsze dwie funkcje nie działąją prawidłowo jeszcze. Proszę o zweryfikowanie czy wogóle moj tok myślenia jest dobry i co poprawić :)
def sum_areas(*figures: list) -> float:
    for figure in figures:
        total_area = sum(figure.get_area)
        return total_area


@staticmethod
def comparing_areas(area: float) -> str:
    if area >= total_area:
        print("It is enough wall paint to cover all this figures")
    else:
        print("Sorry, you have to buy more wall paint.")


def main():
    circle1 = Circle(25)
    circle2 = Circle(5)
    circle3 = Circle(10)
    triangle1 = Triangle(5, 5)
    triangle2 = Triangle(8, 8)
    triangle3 = Triangle(12, 2)
    rectangle1 = Rectangle(2, 8)
    rectangle2 = Rectangle(2, 95)
    rectangle3 = Rectangle(180, 25)

    print(circle1.get_area())
    print(circle2.get_area())
    print(circle3.get_area())
    print(triangle1.get_area())
    print(triangle2.get_area())
    print(triangle3.get_area())
    print(rectangle1.get_area())
    print(rectangle2.get_area())
    print(rectangle3.get_area())

    # tu jest ten moment kiedy nie działa i nie wiem co dalej:(

    print("this is sum area")
    print(sum_areas([circle1, rectangle3, triangle2]))
    print(comparing_areas(25))


if __name__ == "__main__":
    main()
