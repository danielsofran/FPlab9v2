'''
Created on 23 nov. 2021

@author: Daniel
'''

class Film(object):
    '''
    classdocs
    '''


    def __init__(self, id, titlu, descriere, gen):
        '''
        Constructor
        '''
        self.__id = id
        self.__titlu = titlu
        self.__descriere = descriere
        self.__gen = gen

    def get_id(self):
        return self.__id


    def get_titlu(self):
        return self.__titlu


    def get_descriere(self):
        return self.__descriere


    def get_gen(self):
        return self.__gen
    

    def set_titlu(self, value):
        self.__titlu = value


    def set_descriere(self, value):
        self.__descriere = value


    def set_gen(self, value):
        self.__gen = value

    id = property(get_id, None, None, None)
    titlu = property(get_titlu, set_titlu, None, None)
    descriere = property(get_descriere, set_descriere, None, None)
    gen = property(get_gen, set_gen, None, None)

    def show(self):
        return f"Id:{self.id}, Titlu:{self.titlu}, Descriere:{self.descriere}, Gen:{self.gen}"

    def __str__(self):
        return f"{self.id},{self.titlu},{self.descriere},{self.gen}"

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return self.id
    
    @classmethod
    def fromStr(cls, str):
        sir = str.split(',')
        return cls(int(sir[0]), sir[1], sir[2], sir[3])
        