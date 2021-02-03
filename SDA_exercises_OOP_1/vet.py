from python_intermediate_training.SDA_exercises_OOP_1.cat import Cat
from python_intermediate_training.SDA_exercises_OOP_1.dog import Dog
from python_intermediate_training.SDA_exercises_OOP_1.animal import Animal


class Vet():

    @staticmethod
    def say_cat_hello(cat: Cat) -> str:
        return f'Witaj {cat.cat_name}'

    @staticmethod
    def say_dog_hello(dog: Dog) -> str:
        return f'Witaj {dog.dog_name}'

    @staticmethod
    def say_animal_hello(animal: Animal):
        return f"Witaj {animal.animal_name}"
