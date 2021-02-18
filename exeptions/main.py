from python_intermediate_training.exeptions.exercises import case_1, case_2, case_3, case_4, case_6, case_7


def main():
    print('Start up')
    #  wywołanie case_2
    # try:
    #     case_2('')
    # except ValueError as ve:
    #     print(f'{ve.args} returned')

    # wywołanie case_3
    # result = case_3(11, 0)
    # print(result)

    # wywołanie case_4
    #     dictionary = {
    #         "items": ["butter", "bread", "cheese"]
    #     }
    #     case_4(dictionary)

    #  wywołanie case_4_2

    #  wywołanie case_5

    # wywołanie case_6
    # try:
    #     case_6()
    # except NotImplementedError as n:
    #     print(f'Exception caught {n.args}')

    #  wywołanie case_7
    case_7()

    print('Finish')


if __name__ == '__main__':
    main()
