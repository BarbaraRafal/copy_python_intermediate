from abc import ABC


class Animal(ABC):

    def __init__(self, animal_name):
        self._animal_name = animal_name

    @property
    def animal_name(self):
        return self._animal_name
