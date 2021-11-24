from Domain.client import Client
from Exceptii.exceptions import ServiceError
from Validator.validator import ValidatorClient

class ServiceClient:
    def __init__(self, repo):
        self.__repo = repo

    def adauga(self, id, nume, cnp):
        client = Client(id, nume, cnp)
        ValidatorClient.valid(client)
        self.__repo.adauga(client)

    def stergere(self, id):
        client = Client(id, "nume", "1111111111111")
        ValidatorClient.valid(client)
        self.__repo.stergere(id)

    def modificare(self, id, nume, cnp):
        client = Client(id, nume, cnp)
        ValidatorClient.valid(client)
        self.__repo.modificare(id, client)

    def cautare(self, id):
        client = Client(id, "nume", "1111111111111")
        ValidatorClient.valid(client)
        rez = []
        for elem in self.__repo.get_all():
            if elem.id == id:
                return elem
        if len(rez) == 0:
            raise ServiceError("Nu exista astfel de clienti!")

    def cautare_nume(self, nume):
        client = Client(1, nume, "1111111111111")
        ValidatorClient.valid(client)
        rez = []
        for elem in self.__repo.get_all():
            if elem.nume == nume:
                rez.append(elem)
        if len(rez) == 0:
            raise ServiceError("Nu exista astfel de clienti!")
        return rez

    def cautare_cnp(self, cnp):
        client = Client(1, "nume", cnp)
        ValidatorClient.valid(client)
        rez = []
        for elem in self.__repo.get_all():
            if elem.cnp == cnp:
                rez.append(elem)
        if len(rez) == 0:
            raise ServiceError("Nu exista astfel de clienti!")
        return rez

    def vizualizare(self):
        return self.__repo.get_all()


