import sys


def case_1():
    # given
    list_of_numbers = [1, 5, 8, 10, 21]
    # when
    print('Case_1 before')
    # then; wersja pierwsza
    try:
        result = list_of_numbers[5]
    except IndexError as ie:
        print(f'Exception couht {ie.args}')
    except Exception as exp:
        print(f'Exception cought {exp.args}')

    print('Case_1 after')

    # then; wersja druga
    try:
        result = list_of_numbers[5]
    except (IndexError, Exception) as e:
        print(f'Exception cought by touple {e.args}')


def case_2(name: str):
    if len(name) <= 0:
        raise ValueError('String is empty.')
    print(f"Given name is: {name}")


def case_3(number: int, divisor: int) -> float:
    result = 0
    try:
        result = number / divisor
    except ZeroDivisionError as zde:
        print(f'Nie dziel przez zero')
        result = sys.float_info.max
        # result = float(sys.maxsize)
    return result


def case_4(dictionary: dict):
    key = 'items'
    try:
        items: list = dictionary[key]
        for item in items:
            print(item)
    except KeyError as ke:
        print(f'keyword {key} not found, more informations {ke.args}')


def case_4_v2(dictionary: dict):
    key = 'items'
    items: list = dictionary.get(key, [])
    for item in items:
        print(item)
    if item not in items:
        print('Key does not exist or list is empty')


def case_6():
    raise NotImplementedError("Solved future")


def case_7():
    fd = None
    try:
        fd = open('C:\\aaa.txt')
    except IOError as i:
        print(f'Exception caught {i.args}')
        raise NotImplementedError()
    finally:  # wykonuje sie zawsze chyba ze w srodku jest wyjatek w finally
        print("finally run")
        if fd:
            print("File descriptor closing")
            fd.close()

            # finally łaczy sie z try zawsze( moze byc tez except, nie musi) i wykonuje sie zawsze


def case_7_v2():
    try:
        with open('C:\\aaa.txt') as fd:  # context_manager
            print("File is open")
    except IOError as i:
        print(f'Exception caught {i.args}')
