from python_intermediate_training.SDA_exercises_OOP_1.animal import Animal

class Dog(Animal):
    def __init__(self, dog_name: str, dog_sound: str):
        super().__init__(dog_name)
        self.dog_name = dog_name
        self.dog_sound = dog_sound
        self._animal_name = dog_name # przypisanie imienia psa do imienia zwierzecia, ktore jest parametrem w metodzie say_hello_animal w klasie Animal

    def make_sound(self) -> str:
        return f'Dog {self.dog_name} makes {self.dog_sound}'

