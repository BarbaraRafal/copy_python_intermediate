from python_intermediate_training.SDA_exercises_OOP_2_1_10.employee import Employee
from datetime import date


class Manager(Employee):
    def __init__(self, name: str, surname: str, birthday: date, salary: float):
        super().__init__(name, surname, birthday, salary)
        self._salary = salary * 1.1

    @property
    def get_salary(self):
        return self._salary

    @get_salary.setter
    def get_salary(self, value: float):
        self._salary = value * 1.1

    def who_am_i(self):
        print(f'Jestem manager {self._name} {self._surname} i zarabiam {self._salary}')
