from Domain.client import Client
from Exceptii.exceptions import ServiceError
from Validator.validator import ValidatorClient

class ServiceClient:
    def __init__(self, repo):
        self.__repo = repo

    def adauga(self, id, nume, cnp):
        client = Client(id, nume, cnp)
        ValidatorClient.valid(client)
        self.__repo.adauga(Client)

    def stergere(self, id):
        client = Client(id, "nume", "1111111111111")
        ValidatorClient.valid(client)
        self.__repo.stergere(id)

    def modificare(self, id, nume, cnp):
        client = Client(id, nume, cnp)
        ValidatorClient.valid(Client)
        self.__repo.modificare(id, client)

    def cautare(self, id):
        film = Client(id, "nume", "1111111111111")
        ValidatorClient.valid(film)
        rez = []
        for elem in self.__repo.get_all():
            if elem.id == id:
                rez.append(elem)
        if len(rez) == 0:
            raise ServiceError("Nu exista astfel de clienti!")
        return rez

    def vizualizare(self):
        return self.__repo.get_all()


