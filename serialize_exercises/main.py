from python_intermediate_training.serialize_exercises.pickle_training import pickle_write
from python_intermediate_training.serialize_exercises.pickle_training import pickle_read


def main():
    abc = ['bread', 'butter', 'cola']
    pickle_write(abc)
    list_of_strings = pickle_read()
    print(list_of_strings)


if __name__ == "__main__":
    main()
