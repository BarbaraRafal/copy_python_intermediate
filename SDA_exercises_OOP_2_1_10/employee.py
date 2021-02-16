from python_intermediate_training.SDA_exercises_OOP_2_1_10.person import Person
from datetime import date


class Employee(Person):

    def __init__(self, name: str, surname: str, birthday: date, salary: float):
        birthday = self.check_birthday(birthday)
        super().__init__(name, surname, birthday)
        self._salary = salary

    @property
    def get_salary(self):
        return self._salary

    @get_salary.setter
    def get_salary(self, value: float):
        self._salary = value

    @property
    def get_birthday(self):
        return self._birthday

    @get_birthday.setter
    def get_birthday(self, value: date):
        value = self.check_birthday(value)
        self._birthday = value

    @staticmethod
    def check_birthday(value: date) -> date:
        if value > date(year=2020, month=12, day=31) or value < date(year=1900, month=12, day=31):
            value = date(0, 0, 0)
        return value

    def who_am_i(self):
        print(f'Nazywam się {self._name} {self._surname} i zarabiam {self._salary} złotych')
