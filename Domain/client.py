class Client(object):
    def __init__(self, id, titlu, cnp):
        self.__id = id
        self.__nume = titlu
        self.__cnp = cnp

    def get_id(self):
        return self.__id


    def get_nume(self):
        return self.__nume


    def get_cnp(self):
        return self.__cnp


    def set_nume(self, value):
        self.__nume = value


    def set_cnp(self, value):
        self.__cnp = value

    id = property(get_id, None, None, None)
    nume = property(get_nume, set_nume, None, None)
    cnp = property(get_cnp, set_cnp, None, None)

    def show(self):
        return f"Id: {self.id}, Nume: {self.nume}, Cnp: {self.cnp}"
    
    def __str__(self):
        return f"{self.id},{self.nume},{self.cnp}"

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return self.id
    
    @classmethod
    def fromStr(cls, str):
        sir = str.split(',')
        return cls(int(sir[0]), sir[1], sir[2])


