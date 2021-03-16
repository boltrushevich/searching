import os

class Library_helper:

    def __init__(self, words_for_search):
        self.words_for_search = words_for_search
        self.result = []
        self.folder = []
        self.full_adress = []
        self.directory = os.walk('C:\\Users\\User\\Downloads\\Python\\Lessons\\books')

    def direct(self):
        for i in self.directory:
            self.folder.append(i)

    def fold(self):
        for address, dirs, files in self.folder:
            for file in files:
                self.full_adress.append(address + '\\' + file)

    def searching(self):
        try:
            for i in self.full_adress:
                with open(i, 'r', encoding='cp1251') as file:
                    f = file.read().lower()
                    if self.words_for_search in f:
                        self.result.append(i)
        except UnicodeDecodeError:
            return 'UnicodeDecodeError'

    def __repr__(self):
        print(self.result)


a = Library_helper('чехов')
a.direct()
a.fold()
a.searching()
a.__repr__()


