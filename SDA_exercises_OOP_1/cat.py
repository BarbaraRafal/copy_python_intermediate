from python_intermediate_training.SDA_exercises_OOP_1.movable import Movable
from python_intermediate_training.SDA_exercises_OOP_1.animal import Animal


class Cat(Animal, Movable):
    def __init__(self, name: str, sound='Miauu', eaten_mouse: int = 0):
        super().__init__(name)
        self.name = name
        self.sound = sound
        self.eaten_mouse = eaten_mouse

    def make_sound(self) -> str:
        return f'Cat {self.name} makes {self.sound}'

    def eat_mouse(self) -> int:
        self.eaten_mouse += 1
        print(f'Cat {self.name} ate {self.eaten_mouse}. I was very hungry:)')
        return self.eaten_mouse

    def move(self):
        print("Idę")
