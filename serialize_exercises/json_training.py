import json


def write_json_to_file():
    json_list = [
        {"name": "Barbara"},
        {"name": "Kazimierz"},
        {"name": "Krzysztof"}
    ]

    try:
        with open("./training.json", "w") as fd:  # tworzy plik .json, a fd to deskryptor do pliku
            json.dump(json_list, fd, indent=2)  # uzyway biblioteki json i metoda dump zebu zapisac jsona do pliku
            # podajemy w ciele dane do zapisu ( lista) i gdzie (fd) indend 2 format do json
    except(IOError, Exception) as e:
        print(f"Problem with writing to file. More info {e.args}")
