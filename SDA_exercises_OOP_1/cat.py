from python_intermediate_training.SDA_exercises_OOP_1.movable import Movable
from python_intermediate_training.SDA_exercises_OOP_1.animal import Animal


class Cat(Animal, Movable):
    def __init__(self, cat_name: str, sound='Miauu', eaten_mouse: int = 0):
        super().__init__(cat_name)
        self.cat_name = cat_name
        self.sound = sound
        self.eaten_mouse = eaten_mouse
        self._animal_name = cat_name # przypisanie imienia kota do imienia zwierzecia, ktore jest parametrem w metodzie say_hello_animal w klasie Animal


    def make_sound(self) -> str:
        return f'Cat {self.cat_name} makes {self.sound}'

    def eat_mouse(self) -> int:
        self.eaten_mouse += 1
        print(f'Cat {self.cat_name} ate {self.eaten_mouse}. I was very hungry:)')
        return self.eaten_mouse

    def move(self):
        print("idę")
