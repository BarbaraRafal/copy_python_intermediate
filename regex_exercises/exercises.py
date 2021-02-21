import re


def exercise_1():
    print('Write number here:')
    value = input()
    expression = '[0-9]+'
    if re.fullmatch(expression, value):
        print("found number")
        if int(value) % 2 == 0:
            print("This is event number")
        else:
            print("This number is odd")
    else:
        print("incorrect input")


def exercise_2():
    print('Write postal code:')
    value = input()
    expression = '[0-9]{2}-[0-9]{3}'
    if re.fullmatch(expression, value):
        print("This postal code is correct")
    else:
        print("This postal code is incorrect")


