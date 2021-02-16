from python_intermediate_training.SDA_exercises_OOP_1.animal import Animal
from python_intermediate_training.SDA_exercises_OOP_1.mammal import Mammal
from python_intermediate_training.SDA_exercises_OOP_1.canidae import Canidae


class Dog(Animal, Mammal, Canidae):
    def __init__(self, name: str, sound: str):
        Animal.__init__(self, name)
        self.name = name # to podobno można usunąc bo zachodzi polimorfizm i mamy tu cześć wspólną
        self.sound = sound

    def make_sound(self) -> str:
        return f'Dog {self.name} makes {self.sound}'
