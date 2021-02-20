from python_intermediate_training.decorators.exercise2 import read_file


def main():
    # wywołąnie exercise 1
    # a, b = print_hello_world(1, 2)
    # print(f'In main: {a} {b}')

    #  exercise 1
    # def wrap_before_and_after(func):
    #     def wrapper(*args, **kwargs):
    #         print('Before')
    #         result = func(*args, **kwargs)
    #         print('After')
    #         return result
    #
    #     return wrapper
    #
    #
    # @wrap_before_and_after
    # def print_hello_world(a, b):
    #     print("Hello world!")
    #     print(f'{a, b}')
    #     return a, b

    read_file(file_path='./abc.txt')


if __name__ == '__main__':
    main()
