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
    expression = '([A-Z0-9!@#\\$%\\^&\\*]{5}\\-){4}[A-Z0-9!@#\\$%\\^&\\*]'  ### to wyrażenie skopiowane z odpowiedzi nie działa
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
    from collections import Counter
    my_text = """Drogi Marszałku, Wysoka Izbo. PKB rośnie. Z pełną odpowiedzialnością mogę" 
stwierdzić iż realizacja określonych zadań stanowionych przez organizację. Dalszy
rozwój jest ważne zadanie w większym stopniu tworzenie odpowiednich warunków
aktywizacji. Często niezauważanym szczegółem jest to, że zakres i rozwijanie
struktur pociąga za najważniejszy punkt naszych działań obierzemy praktykę, nie zaś
teorię, okazuje się jasne."""

    splited_text = my_text.split()

    # # liczy słowa
    splited_text_list = []
    for word in splited_text:
        splited_text_list.append(word)
        amount_of_words = splited_text_list.count(word
    print(f"Liczba słów w tekście to:{amount_of_words}")

    ## wyswietla najdłuże i najkrótsze słowo
    longest_word = max(splited_text, key=len)
    print(f"Najdłuższe słowo to:{longest_word} a jego długość to:{len(longest_word)}")

    shortest_word = min(splited_text, key=len)
    print(f"Najkrótsze słowo to:{shortest_word} a jego długość to: {len(shortest_word)}")
