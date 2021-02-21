def exercise_1():
    names = ["Barbara", "Krzysztof", "Kazimierz", "Lilianna", "Grisza", "Indira"]
    print("case A")

    result_a = sorted(names, key=lambda name: len(name))
    print(result_a)

    print("case B")
    result_b = sorted(names, key=lambda name: len(name), reverse=True)
    print(result_b)

    print("case C")
    result_c = sorted(names, key=lambda name: name[0])
    print(result_c)
