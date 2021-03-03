from contextlib import contextmanager


@contextmanager
def open_file(path: str, mode='a'):
    print("opening file in progress...")
    fd = open(path, mode)
    yield fd  # zwracmy to do with
    fd.close()  # tu musimy zawołac to co sie dzieje po wyjsciu  with
    print("file is closing...")


def exercise_1():
    try:
        with open_file("./file_to_open.txt") as fd:
            fd.write("dopisz mnie do pliku")
    except IOError as ioe:
        print(f" Problem with writing to file {ioe.args}")




