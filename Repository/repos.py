from Repository.repository import Repository, FileRepository
from Exceptii.exceptions import RepositoryError
from Domain.film import Film
from Domain.client import Client
from Domain.inchirieredto import InchiriereDto

class RepoFilm(Repository):
    def __init__(self):
        super(RepoFilm, self).__init__(Film)

class RepoClient(Repository):
    def __init__(self):
        super(RepoClient, self).__init__(Client)

class FileRepoFilm(FileRepository):
    def __init__(self, file):
        super(FileRepoFilm, self).__init__(Film, file)

class FileRepoClient(FileRepository):
    def __init__(self, file):
        super(FileRepoClient, self).__init__(Client, file)

class RepoInchiriere(Repository):
    def __init__(self):
        super(RepoInchiriere, self).__init__(InchiriereDto)

    def stergere(self, inchiriere):
        for elem in self._container:
            if elem == inchiriere:
                self._container.remove(inchiriere)
                break
        else:
            raise RepositoryError("Inchirierea data nu a fost gasita!")

class FileRepoInchiriere(FileRepository):
    def __init__(self, file):
        super(FileRepoInchiriere, self).__init__(InchiriereDto, file)

    def stergere(self, inchiriere):
        self._read_from_file()
        super(FileRepoInchiriere, self).stergere(inchiriere)
        self._write_to_file()