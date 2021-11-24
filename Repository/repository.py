from Exceptii.exceptions import RepositoryError, DuplicatedIDError

class Repository:
    def __init__(self, tip):
        self._tip = tip
        self._container = []

    def __len__(self):
        return len(self._container)

    def get_all(self):
        return self._container[:]

    def cauta_id(self, id):
        for elem in self._container:
            if elem.id == id:
                return elem
        raise RepositoryError("Elementul cu id-ul dat nu a fost gasit!")

    def adauga(self, obj):
        if not isinstance(obj, self._tip):
            print(obj)
            raise RepositoryError("Tip gresit!")
        for elem in self._container:
            if elem == obj:
                raise DuplicatedIDError("Id duplicat!")
        self._container.append(obj)

    def stergere(self, id):
        for elem in self._container:
            if elem.id == id:
                self._container.remove(elem)
                break
        else:
            raise RepositoryError("Elementul cu acest id nu a fost gasit!")

    def modificare(self, id, obj):
        gasit = False
        for i in range(len(self._container)):
            if self._container[i].id == id:
                self._container[i] = obj
                gasit = True
            elif self._container[i].id == obj.id:
                raise DuplicatedIDError("Id duplicat la modificare!")
        if not gasit: raise RepositoryError("Elementul nu poate fi gasit!")

class FileRepository(Repository):
    def __init__(self, tip, file):
        Repository.__init__(self, tip)
        self.__file = file

    def __read_from_file(self):
        with open(self.__file, 'r') as f:
            self._container = []
            for line in f:
                line = line.strip()
                obj = self._tip.fromStr(line)
                self._container.append(obj)

    def __write_to_file(self):
        with open(self.__file, 'w') as f:
            for elem in self._container:
                f.write(str(elem)+"\n")

    def __len__(self):
        self.__read_from_file()
        return Repository.__len__(self)

    def get_all(self):
        self.__read_from_file()
        return Repository.get_all(self)

    def cauta_id(self, id):
        self.__read_from_file()
        return Repository.cauta_id(self, id)

    def adauga(self, obj):
        self.__read_from_file()
        super(FileRepository, self).adauga(obj)
        self.__write_to_file()

    def stergere(self, id):
        self.__read_from_file()
        super(FileRepository, self).stergere(id)
        self.__write_to_file()

    def modificare(self, id, obj):
        self.__read_from_file()
        super(FileRepository, self).modificare(id, obj)
        self.__write_to_file()
