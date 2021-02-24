class Complex:
    def __init__(self, a, b=0):
        self.a = a
        self.b = b

    def show(self):
        if self.b > 0:
            print(f'{self.a} + {self.b} * i')
        elif self.b == 0:
            print(f'{self.a}')
        else:
            print(f'{self.a} {self.b} * i')

    def is_equal_to(self):
        pass

