from Domain.film import Film
from Exceptii.exceptions import ServiceError
from Validator.validator import ValidatorFilm

class ServiceFilm:
    def __init__(self, repo): # service de filme, repo - repository-ul asociat
        self.__repo = repo

    def adauga(self, id, titlu, descriere, gen): # creare, validare, adaugare de film
        film = Film(id, titlu, descriere, gen)
        ValidatorFilm.valid(film)
        self.__repo.adauga(film)

    def stergere(self, id): # validare id, stergere film dupa id
        film = Film(id, "titlu", "descriere", "gen")
        ValidatorFilm.valid(film)
        self.__repo.stergere(id)

    def modificare(self, id, titlu, descriere, gen): # actualizare film dupa id, validare actualizare
        film = Film(id, titlu, descriere, gen)
        ValidatorFilm.valid(film)
        self.__repo.modificare(id, film)

    def cautare(self, id): # cautare dupa id
        film = Film(id, "titlu", "descriere", "gen")
        ValidatorFilm.valid(film)
        for elem in self.__repo.get_all():
            if elem.id == id:
                return elem
        raise ServiceError("Nu exista astfel de filme!")

    def cautare_titlu(self, titlu): # cautare fupa titlu
        film = Film(1, titlu, "descriere", "gen")
        ValidatorFilm.valid(film)
        rez = []
        for elem in self.__repo.get_all():
            if elem.titlu == titlu:
                rez.append(elem)
        if len(rez) == 0:
            raise ServiceError("Nu exista astfel de filme!")
        return rez

    def cautare_descriere(self, descriere): # cautare dupa descriere
        film = Film(1, "titlu", descriere, "gen")
        ValidatorFilm.valid(film)
        rez = []
        for elem in self.__repo.get_all():
            if elem.descriere == descriere:
                rez.append(elem)
        if len(rez) == 0:
            raise ServiceError("Nu exista astfel de filme!")
        return rez

    def cautare_gen(self, gen): # cautare dupa gen
        film = Film(1, "titlu", "descriere", gen)
        ValidatorFilm.valid(film)
        rez = []
        for elem in self.__repo.get_all():
            if elem.gen == gen:
                rez.append(elem)
        if len(rez) == 0:
            raise ServiceError("Nu exista astfel de filme!")
        return rez

    def vizualizare(self): # functie care returneaza toate filmele
        return self.__repo.get_all()


