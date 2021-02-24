from datetime import date


class Person:
    def __init__(self, name: str, surname: str, birthday: date, sex: str):
        self._name = name
        self._surname = surname
        self._birthday = birthday
        self._sex = sex

    @property
    def get_name(self):
        return self._name

    @get_name.setter
    def get_name(self, value: str):
        self._name = value

    @property
    def get_surname(self):
        return self._surname

    @get_surname.setter
    def get_surname(self, value: str):
        self._surname = value

    @property
    def get_birthday(self):
        return self._birthday

    @get_birthday.setter
    def get_birthday(self, value: date):
        self._birthday = value

    @property
    def get_sex(self):
        return self._sex

    @get_sex.setter
    def get_sex(self, value: str):
        self._sex = value
