class Dog:
    def __init__(self, dog_name: str, dog_sound: str):
        self.dog_name = dog_name
        self.dog_sound = dog_sound

    def make_sound(self) -> str:
        return f'Dog {self.dog_name} makes {self.dog_sound}'

