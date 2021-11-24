from Domain.film import Film
from Exceptii.exceptions import ServiceError
from Validator.validator import ValidatorFilm

class ServiceFilm:
    def __init__(self, repo):
        self.__repo = repo

    def adauga(self, id, titlu, descriere, gen):
        film = Film(id, titlu, descriere, gen)
        ValidatorFilm.valid(film)
        self.__repo.adauga(film)

    def stergere(self, id):
        film = Film(id, "titlu", "descriere", "gen")
        ValidatorFilm.valid(film)
        self.__repo.stergere(id)

    def modificare(self, id, titlu, descriere, gen):
        film = Film(id, titlu, descriere, gen)
        ValidatorFilm.valid(film)
        self.__repo.modificare(id, film)

    def cautare(self, id):
        film = Film(id, "titlu", "descriere", "gen")
        ValidatorFilm.valid(film)
        for elem in self.__repo.get_all():
            if elem.id == id:
                return elem
        raise ServiceError("Nu exista astfel de filme!")

    def cautare_titlu(self, titlu):
        film = Film(1, titlu, "descriere", "gen")
        ValidatorFilm.valid(film)
        rez = []
        for elem in self.__repo.get_all():
            if elem.titlu == titlu:
                rez.append(elem)
        if len(rez) == 0:
            raise ServiceError("Nu exista astfel de filme!")
        return rez

    def cautare_descriere(self, descriere):
        film = Film(1, "titlu", descriere, "gen")
        ValidatorFilm.valid(film)
        rez = []
        for elem in self.__repo.get_all():
            if elem.descriere == descriere:
                rez.append(elem)
        if len(rez) == 0:
            raise ServiceError("Nu exista astfel de filme!")
        return rez

    def cautare_gen(self, gen):
        film = Film(1, "titlu", "descriere", gen)
        ValidatorFilm.valid(film)
        rez = []
        for elem in self.__repo.get_all():
            if elem.gen == gen:
                rez.append(elem)
        if len(rez) == 0:
            raise ServiceError("Nu exista astfel de filme!")
        return rez

    def vizualizare(self):
        return self.__repo.get_all()


