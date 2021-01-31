from SDA_exercises_OOP_1.cat import Cat


def main():
    cat1 = Cat("Grisza")
    sound: str = cat1.make_sound()
    print(sound)


if __name__ == "__main__":
    main()
