from SDA_exercises_OOP_1.cat import Cat
from SDA_exercises_OOP_1.dog import Dog


def main():
    cat1 = Cat("Grisza", "Maiuuu")
    cat2 = Cat("Indira", "Mrrrr")
    cat3 = Cat("Felix", "Grrrrr")
    cat4 = Cat("Garfield", "Brrrrr")

    dog1 = Dog("Tesla", "Auuuu")
    dog2 = Dog("Czarny Latek", "Hauhau")

    animal_list = []
    animal_list.append(cat1)
    animal_list.append(cat2)
    animal_list.append(cat3)
    animal_list.append(cat4)
    animal_list.append(dog1)
    animal_list.append(dog2)

    for animal in animal_list:
        print(animal.make_sound())


    print(f"Now {cat1.cat_name} is eating")
    cat1.eat_mouse()
    cat1.eat_mouse()
    cat1.eat_mouse()
    cat1.eat_mouse()
    cat1.eat_mouse()
    print(f"Now {cat2.cat_name} is eating")
    cat2.eat_mouse()


if __name__ == "__main__":
    main()
