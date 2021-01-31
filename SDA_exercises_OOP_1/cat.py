class Cat:
    def __init__(self, cat_name: str):
        self.cat_name = cat_name

    def make_sound(self) -> str:
        return f'Name {self.cat_name} makes miau'
