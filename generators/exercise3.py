class Iterable:
    def __init__(self, number):
        self.number = number
        self.generated_number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.generated_number >= self.number - 1:
            raise StopIteration
        self.generated_number += 1
        return self.generated_number
