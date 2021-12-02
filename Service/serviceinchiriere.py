import functools

from Domain.inchirieredto import InchiriereDto
from Validator.validator import ValidatorInchiriereDto

class ServiceInchiriere:
    def __init__(self, repoinchiriere, repoclient, repofilm): # constructor
        self.__repoinchiriere = repoinchiriere
        self.__repofilm = repofilm
        self.__repoclient = repoclient

    def inchiriaza(self, id_client, id_film): # inchirieaza un film
        self.__repoclient.cauta_id(id_client)
        self.__repofilm.cauta_id(id_film)
        inchirieredto = InchiriereDto(id_client, id_film)
        ValidatorInchiriereDto.valid(inchirieredto)
        self.__repoinchiriere.adauga(inchirieredto)

    def returneaza(self, id_client, id_film): # returneaza un film
        self.__repoclient.cauta_id(id_client)
        self.__repofilm.cauta_id(id_film)
        inchirieredto = InchiriereDto(id_client, id_film)
        self.__repoinchiriere.stergere(inchirieredto)

    def __filme_per_client(self): # asociaza filmele clientilor
        rez = {}
        erase_list = []
        for inchiriere in self.__repoinchiriere.get_all():
            try:
                film = self.__repofilm.cauta_id(inchiriere.id_film)
                client = self.__repoclient.cauta_id(inchiriere.id_client)
            except:
                erase_list.append(inchiriere)
                continue
            if not client in rez:
                rez[client] = []
            rez[client].append(film)
        for elem in erase_list:
            self.__repoinchiriere.stergere(elem)
        return rez

    def __clienti_per_film(self): # asociaza clientii filmelor
        rez = {}
        erase_list = []
        for inchiriere in self.__repoinchiriere.get_all():
            try:
                film = self.__repofilm.cauta_id(inchiriere.id_film)
                client = self.__repoclient.cauta_id(inchiriere.id_client)
            except:
                erase_list.append(inchiriere)
                continue
            if not film in rez:
                rez[film] = []
            rez[film].append(client)
        for elem in erase_list:
            self.__repoinchiriere.stergere(elem)
        return rez

    def raport_clienti_cu_filme_dupa_nume(self): # clientii ordonati dupa nume, nr de filme inchiriate, cu filmele respective
        rel = self.__filme_per_client()
        keys = sorted(rel, key=lambda client: client.nume)
        rez = {}
        for elem in keys:
            rez[elem] = rel[elem]
        return rez

    def raport_clienti_cu_filme_dupa_nr_filmelor(self): # clientii ordonati dupa nume, nr de filme inchiriate, cu filmele respective
        rel = self.__filme_per_client()
        keys = sorted(rel, key=lambda client: len(rel[client]))
        rez = {}
        for elem in keys:
            rez[elem] = rel[elem]
        return rez

    def raport_filme_inchiriate(self): # cele mai inchiriate filme, returneaza lista de filme
        rez = self.__clienti_per_film()
        rez = sorted(rez, key=lambda film: len(rez[film]), reverse=True)
        return rez

    def raport_primii_clienti_cu_cele_mai_multe_filme(self): # primiii 30% clienti_cu_cele_mai_multe_filme
        '''
            returneaza lista de clienti
            :rtype: list of tuples (nume_client, nr_de_filme_inchiriate)
        '''
        rel = self.__filme_per_client()
        keys = sorted(rel, key=lambda client: len(rel[client]), reverse=True)
        rez = []
        length = round(len(rel)*30/100)
        for elem in keys[:length]:
            rez.append((elem.nume, len(rel[elem])))
        return rez

    def raport_cele_mai_putin_inchiriate_filme_care_incep_cu_un_string_dat(self, string_dat):
        # 50% cele_mai_putin_inchiriate_filme_care_incep_cu_un_string_dat
        rel = self.__clienti_per_film()
        def cmp(film1, film2):
            if len(rel[film1]) > len(rel[film2]):
                return -1
            elif len(rel[film1]) > len(rel[film2]):
                return 1
            else:
                if film1.titlu < film2.titlu:
                    return -1
                elif film1.titlu > film2.titlu:
                    return 1
                return 0
        filme = sorted(rel, key=functools.cmp_to_key(cmp))
        to_remove = []
        for elem in filme:
            if not elem.titlu.startswith(string_dat):
                to_remove.append(elem)
        for elem in to_remove:
            filme.remove(elem)
        length = round(len(filme) * 50 / 100)
        filme = filme[:length]
        return filme


