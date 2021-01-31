from SDA_exercises_OOP_1.exercise1 import Cat
from SDA_exercises_OOP_1.exercise1 import Dog


def main():
    kitty = Cat()
    kitty.add_cat("Grisza", "Miauuu", 5)
    kitty.add_cat("Indira", "Mrrrrr", 6)
    print(kitty.make_sound())
    print(kitty.eat_mouse())
    print(kitty.get_cat_list())

    puppy = Dog()
    puppy.add_dog("Czarny Latek", "hau hau")
    puppy.add_dog("Tesla", "auuuuuu")
    print(puppy.make_sound())


if __name__ == "__main__":
    main()