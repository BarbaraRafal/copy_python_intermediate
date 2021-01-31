class Cat:
    def __init__(self, cat_name: str, sound='Miauu', eaten_mouse=0):
        self.cat_name = cat_name
        self.sound = sound
        self.eaten_mouse = eaten_mouse

    def make_sound(self) -> str:
        return f'Cat {self.cat_name} makes {self.sound}'

    def eat_mouse(self) -> int:
        self.eaten_mouse += 1
        print(f'Cat {self.cat_name} ate {self.eaten_mouse}. I was very hungry:)')
        return self.eaten_mouse
