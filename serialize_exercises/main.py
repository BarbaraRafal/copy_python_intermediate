# from python_intermediate_training.serialize_exercises.pickle_training import pickle_write
# from python_intermediate_training.serialize_exercises.pickle_training import pickle_read
from python_intermediate_training.serialize_exercises.json_training import write_json_to_file, read_json_from_file
from python_intermediate_training.serialize_exercises.human import Human


def main():
    # abc = ['bread', 'butter', 'cola']
    # pickle_write(abc)
    # list_of_strings = pickle_read()
    # print(list_of_strings)

    # json training below
    # write_json_to_file()
    # print(read_json_from_file())

    # h1 = Human(30, "Jan", "Kowalski")
    # h2 = Human(25, "Anna", "Kowalska")
    # h3 = Human(40, "Tomasz", "Nowak")
    #
    # humans = [h1, h2, h3]
    #
    # write_json_to_file

    humans = read_json_from_file()
    for human in humans:
        print(human)

    # print(json_human_from_file())


if __name__ == "__main__":
    main()
