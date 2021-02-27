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
    expression = r'[0-9]{2}-[0-9]{3}'
    if re.fullmatch(expression, value):
        print("This postal code is correct")
    else:
        print("This postal code is incorrect")


def exercise_3():
    print('Write your login:')
    value = input()
    expression = '[a-zA-Z0-9]{8,16}'
    if re.fullmatch(expression, value):
        print("This login is correct")
    else:
        print("This login is incorrect")


def exercise_4():
    print('Write your text:')
    value = input()
    expression = '.*ala.*'
    if re.fullmatch(expression, value):
        print("Your text contains 'ala'.")
    else:
        print("Your text doesn't contain 'ala'.")


def exercise_5():
    print('Write date: ')
    value = input()
    expression = '[0-9]{2}.[0-9]{2}.[0-9]{4}.*'  # mozna tu wpisac dzien np 32 i miesiąc 15 i bedzie ok i dopisać lub nie
    if re.fullmatch(expression, value):
        print("Your date is correct.")
    else:
        print("Your date is incorrect.")


def exercise_6():
    print('Write your serial number: ')
    value = input()
    expression = '[A-Z]{3}[0-9]{5}[a-z]{1}[A-Z]{1}'
    if re.fullmatch(expression, value):
        print("Your serial number is correct.")
    else:
        print("Your serial number is incorrect.")


def exercise_7():
    print('Write your serial number: ')
    value = input()

    expression = r'([A-Z0-9!@#\$%\^&\*]{5}-){4}[A-Z0-9!@#\$%\^&\*]{5}'
    if re.fullmatch(expression, value):
        print("Your serial number is correct.")
    else:
        print("Your serial number is incorrect.")


def exercise_8():
    print('Write an invoice number: ')
    value = input()
    expression = 'FV/[0-9]{1,4}/[0-9]{2}/[0-9]{4}'
    if re.fullmatch(expression, value):
        print("Your invoice number is correct.")
    else:
        print("Your invoice number is incorrect.")


def exercise_9():
    my_text = """Drogi Marszałku, Wysoka Izbo. PKB rośnie. Z pełną odpowiedzialnością mogę" 
stwierdzić iż realizacja określonych zadań stanowionych przez organizację. Dalszy
rozwój jest ważne zadanie w większym stopniu tworzenie odpowiednich warunków
aktywizacji. Często niezauważanym szczegółem jest to, że zakres i rozwijanie
struktur pociąga za najważniejszy punkt naszych działań obierzemy praktykę, nie zaś
teorię, okazuje się jasne."""
    # splited_text = my_text.split()
    # print(splited_text)

    # # # liczy słowa
    # amount_of_words = len(splited_text)
    # print(amount_of_words)
    # print(f"Liczba słów w tekście to:{amount_of_words}")
    # # # liczy znaki
    # amount_of_characters = len(my_text)
    # print(f"Liczba znaków w tekście to:{amount_of_characters}")
    #
    # ## liczy srędnią długość wyrazu
    # average_lenght_of_word = amount_of_characters / amount_of_words
    # print(f"Średnia długość wyrazu to: {round(average_lenght_of_word)}")
    #
    # ## wyswietla najdłuże i najkrótsze słowo
    # longest_word = max(splited_text, key=len)
    # print(f"Najdłuższe słowo to:{longest_word} a jego długość to: {len(longest_word)}")
    #
    # shortest_word = min(splited_text, key=len)
    # print(f"Najkrótsze słowo to:{shortest_word} a jego długość to: {len(shortest_word)}")

    ### rozwiązanie Adama
    empty_text = ''

    words_number = my_text.split()  ## zwraca listę
    # print(words_number)
    print(f'Words number: {len(words_number)}')

    char_number = re.split(empty_text, my_text)
    # print(char_number)
    print(f'Characters number: {len(char_number)}')

    average_operation = [len(char_number) for char_number in words_number] # lista zawierajca długość każdego wyrazu
    print(average_operation)
    average = sum(average_operation) / len(average_operation)
    print(f'The average word length is: {average:.2f}')
   # average_operation = [] # dłuższy zapis
    # for char_number in words_number:
    #    average_operation.append(len(char_number))
    # average = sum(average_operation) / len(average_operation)
    # print(f'Average : {average}')

    max_word = [len(char_number) for char_number in words_number]
    print(f'The longest number of characters in a word: {max(max_word)}')

    min_word = [len(char_number) for char_number in words_number]
    print(f'The shortest number of characters in a word: {min(min_word)}')
