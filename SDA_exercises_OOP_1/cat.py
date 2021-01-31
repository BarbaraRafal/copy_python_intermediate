class Cat:
    def __init__(self, cat_name: str, sound='Miauu'):
        self.cat_name = cat_name
        self.sound = sound


    def make_sound(self) -> str:
        return f'Cat {self.cat_name} makes {self.sound}'
