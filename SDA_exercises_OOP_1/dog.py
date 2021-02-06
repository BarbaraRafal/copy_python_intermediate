from python_intermediate_training.SDA_exercises_OOP_1.animal import Animal


class Dog(Animal):
    def __init__(self, name: str, sound: str):
        super().__init__(name)
        self.name = name # to podobno można usunąc bo zachodzi polimorfizm i mamy tu cześć wspólną
        self.sound = sound

    def make_sound(self) -> str:
        return f'Dog {self.name} makes {self.sound}'
