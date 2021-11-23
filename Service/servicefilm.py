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

    def vizualizare(self):
        return self.__repo.get_all()


