from python_intermediate_training.generators.exercise3 import Iterable
from python_intermediate_training.generators.exercise_4 import exercise_4
from python_intermediate_training.generators.exercise_5 import reader_line_by_line


def iterator_ex_1():
    dictionary = {
        'a': 1,
        'b': 2,
        'c': 3
    }

    for key in dictionary.keys():
        print(key)

    for value in dictionary.values():
        print(value)


def number_creator(n):
    list_of_numbers = []
    for number in range(n):
        list_of_numbers.append(number)
    return list_of_numbers


def iterator_ex_2(n):
    print('exercise2')
    import sys
    result_list = number_creator(n)
    print(f'Size of list in bytes: {sys.getsizeof(result_list)} ')
    result = sum(result_list)
    print(f'size of one number in bytes : {sys.getsizeof(result)}')
    print(result)


def iterator_ex_3(n):
    print('exercise3')
    import sys
    iterator_list = Iterable(n)
    print(f'Size of iterator in bytes: {sys.getsizeof(iterator_list)} ')
    result = sum(iterator_list)
    print(f'size of one number in bytes : {sys.getsizeof(result)}')
    print(result)


def main():
    # # iterator_ex_1()
    # print("exercise 2")
    # iterator_ex_2(100000)
    # print('exercise 3')
    # iterator_ex_3(100000)
    # print(file_reader())

    # ex 4
    # print("exercise 4")
    # exercise_4()

    #  ex5
    print("exercise5")
    reader_line_by_line()
    # for elements in reader_line_by_line():
    #     print(elements)


if __name__ == "__main__":
    main()
