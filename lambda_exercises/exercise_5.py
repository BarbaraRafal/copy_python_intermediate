from random import randint


def exercise_5():
    int_list = [randint(100, 201) for item in range(20)]
    print(int_list)

    # lista posortowana rosnąco
    asc_int_list = sorted(int_list)
    print(asc_int_list)

    # lista posortowana malejąco
    desc_int_list = sorted(int_list, reverse=True)
    print(desc_int_list)
