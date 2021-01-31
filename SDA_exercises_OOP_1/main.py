from SDA_exercises_OOP_1.cat import Cat


def main():
    cat1 = Cat("Grisza", "Maiuuu")
    cat2 = Cat("Indira", "Mrrrr")
    cat3 = Cat("Felix", "Grrrrr")
    cat4 = Cat("Garfield", "Brrrrr")

    # cats = [cat1, cat2, cat3, cat4]
    # for cat in cats:
    #     print(cat.make_sound())

    cats_list = []
    cats_list.append(cat1)
    cats_list.append(cat2)
    cats_list.append(cat3)
    cats_list.append(cat4)

    for cat in cats_list:
        print(cat.make_sound())






if __name__ == "__main__":
    main()
