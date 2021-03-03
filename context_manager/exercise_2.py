class OpenFileManager:
    def __init__(self, path: str = "", mode='a'):
        self.__source = path
        self.__mode = mode
        self.__fd = None

    @property ## gettery
    def source(self):
        return self.__source

    def get_source(self):
        return self.__source

    @source.setter ## settery
    def source(self, path: str):
        self.__source = path

    def set_source(self, path: str):
        self.__source = path

    def __enter__(self):
        print("Opening file")
        self.__fd = open(self.__source, self.__mode)
        return self.__fd

    def __exit__(self, *args):
        print("Closing file")
        self.__fd.close()


def exercise_2():
    manager = OpenFileManager()
    manager_source = manager.source  # getter
    print(manager_source) # drukujemy ale jest pusty
    manager.source = "./test_file.txt"  # setter ustawiamy sciezke/Ÿród³o
    manager_source = manager.source  # getter znowu pobieramy sciezke
    print(manager_source) # i j¹ drukujemy

    try:
        with manager as fd:
            print("Writing")
            fd.write("Tekst")
    except IOError as e:
        print(f"We have an error: {e.args}")
