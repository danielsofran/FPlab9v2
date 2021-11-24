class Console:
    def __init__(self, servicefilm, serviceclient, serviceinchiriere):
        self.__servicefilm = servicefilm
        self.__serviceclient = serviceclient
        self.__serviceinchiriere = serviceinchiriere

    def __print_menu(self):
        print("filme[adauga|sterge|modifica|vizualizeaza|cauta]",
              "clienti[adauga|sterge|modifica|vizualizeaza|cauta]",
              "inchiriere|returnare",
              "rapoarte:\n\tclienti cu filme ordonati dupa nume"
              "\n\tclienti cu filme ordonati dupa numarul de filme inchiriate"
              "\n\tcele mai inchiriate filme"
              "\n\tprimii 30% clienti cu cele mei multe filme",
              "exit",
              sep='\n')
    #region Film
    def __adauga_film(self):
        id = input("Id: ")
        try:
            id = int(id)
        except ValueError:
            print("Id numeric invalid!")
            return
        titlu = input("Titlu: ")
        descriere = input("Descriere: ")
        gen = input("Gen: ")
        try: self.__servicefilm.adauga(id, titlu, descriere, gen)
        except Exception as ex: print(str(ex))
        else: print("Film adaugat cu succes!")

    def __stergere_film(self):
        id = input("Id: ")
        try: id = int(id)
        except ValueError:
            print("Id numeric invalid!")
            return
        try: self.__servicefilm.stergere(id)
        except Exception as ex: print(str(ex))
        else: print("Film sters!")

    def __modificare_film(self):
        id = input("Id: ")
        try:
            id = int(id)
        except ValueError:
            print("Id numeric invalid!")
            return
        titlu = input("Titlu nou: ")
        descriere = input("Descriere noua: ")
        gen = input("Gen nou: ")
        try: self.__servicefilm.modificare(id, titlu, descriere, gen)
        except Exception as ex: print(str(ex))
        else: print("Film modificat!")

    def __vizualizeaza_film(self):
        lst = self.__servicefilm.vizualizare()
        if len(lst) == 0:
            print("Nu exista filme!")
            return
        for film in lst:
            print(film.show(), sep='\n')

    def __cauta_film(self):
        id = input("Id: ")
        try:
            id = int(id)
        except ValueError:
            print("Id numeric invalid!")
            return
        try: film = self.__servicefilm.cautare(id)
        except Exception as ex: print(str(ex))
        else: print(film.show(), sep='\n')
    #endregion

    # region Client
    def __adauga_client(self):
        id = input("Id: ")
        try:
            id = int(id)
        except ValueError:
            print("Id numeric invalid!")
            return
        nume = input("Nume: ")
        cnp = input("Cnp: ")
        try:
            self.__serviceclient.adauga(id, nume, cnp)
        except Exception as ex:
            print(str(ex))
        else:
            print("Client adaugat cu succes!")

    def __stergere_client(self):
        id = input("Id: ")
        try:
            id = int(id)
        except ValueError:
            print("Id numeric invalid!")
            return
        try:
            self.__serviceclient.stergere(id)
        except Exception as ex:
            print(str(ex))
        else:
            print("Client sters!")

    def __modificare_client(self):
        id = input("Id: ")
        try:
            id = int(id)
        except ValueError:
            print("Id numeric invalid!")
            return
        nume = input("Nume: ")
        cnp = input("Cnp: ")
        try:
            self.__serviceclient.modificare(id, nume, cnp)
        except Exception as ex:
            print(str(ex))
        else:
            print("Client modificat!")

    def __vizualizeaza_client(self):
        lst = self.__serviceclient.vizualizare()
        if len(lst) == 0:
            print("Nu exista clienti!")
            return
        for client in lst:
            print(client.show(), sep='\n')

    def __cauta_client(self):
        id = input("Id: ")
        try:
            id = int(id)
        except ValueError:
            print("Id numeric invalid!")
            return
        try:
            client = self.__serviceclient.cautare(id)
        except Exception as ex:
            print(str(ex))
        else:
            print(client.show(), sep='\n')
    # endregion

    #region Inchirieri Rapoarte
    def __inchiriere(self):
        id_client = input("Id client: ")
        try:
            id_client = int(id_client)
        except ValueError:
            print("Id numeric invalid!")
            return
        id_film = input("Id film: ")
        try:
            id_film = int(id_film)
        except ValueError:
            print("Id numeric invalid!")
            return
        try: self.__serviceinchiriere.inchiriaza(id_client, id_film)
        except Exception as ex: print(str(ex))
        else: print("Inchirierea s-a efectuat cu succes!")

    def __returnare(self):
        id_client = input("Id client: ")
        try:
            id_client = int(id_client)
        except ValueError:
            print("Id numeric invalid!")
            return
        id_film = input("Id film: ")
        try:
            id_film = int(id_film)
        except ValueError:
            print("Id numeric invalid!")
            return
        try:
            self.__serviceinchiriere.returneaza(id_client, id_film)
        except Exception as ex:
            print(str(ex))
        else:
            print("Inchirierea s-a efectuat cu succes!")

    def __raport_clienti_cu_filme_dupa_nume(self):
        rez = self.__serviceinchiriere.raport_clienti_cu_filme_dupa_nume()
        if len(rez) == 0:
            print("Nu exista astfel de inchirieri!")
            return
        for client in rez:
            print(client.show())
            for film in rez[client]:
                print("\t" + film.show())

    def __raport_clienti_cu_filme_dupa_nr_filmelor(self):
        rez = self.__serviceinchiriere.raport_clienti_cu_filme_dupa_nr_filmelor()
        if len(rez) == 0:
            print("Nu exista astfel de inchirieri!")
            return
        for client in rez:
            print(client.show())
            for film in rez[client]:
                print("\t" + film.show())

    def __raport_filme_inchiriate(self):
        rez = self.__serviceinchiriere.raport_filme_inchiriate()
        if len(rez) == 0:
            print("Nu exista astfel de inchirieri!")
            return
        for film in rez:
            print(film.show())

    def __raport_primii_clienti_cu_cele_mai_inchiriate_filme(self):
        rez = self.__serviceinchiriere.raport_primii_clienti_cu_cele_mai_inchiriate_filme()
        if len(rez) == 0:
            print("Nu exista astfel de inchirieri!")
            return
        for pereche in rez:
            print(f"{pereche[0]} a inchiriat {pereche[1]} filme")

    #endregion

    def run(self):
        while True:
            self.__print_menu()
            cmd = input("Introduceti comanda: ")
            cmd = cmd.strip()
            if cmd == "": continue
            elif cmd == "exit": return
            elif cmd == "filme adauga": self.__adauga_film()
            elif cmd == "filme sterge": self.__stergere_film()
            elif cmd == "filme modifica": self.__modificare_film()
            elif cmd == "filme vizualizeaza": self.__vizualizeaza_film()
            elif cmd == "filme cauta": self.__cauta_film()
            elif cmd == "clienti adauga": self.__adauga_client()
            elif cmd == "clienti sterge": self.__stergere_client()
            elif cmd == "clienti modifica": self.__modificare_client()
            elif cmd == "clienti vizualizeaza": self.__vizualizeaza_client()
            elif cmd == "clienti cauta": self.__cauta_client()
            elif cmd == "inchiriere": self.__inchiriere()
            elif cmd == "returnare": self.__returnare()
            elif cmd == "rapoarte clienti cu filme ordonati dupa nume": self.__raport_clienti_cu_filme_dupa_nume()
            elif cmd == "rapoarte clienti cu filme ordonati dupa numarul de filme inchiriate": self.__raport_clienti_cu_filme_dupa_nr_filmelor()
            elif cmd == "rapoarte cele mai inchiriate filme": self.__raport_filme_inchiriate()
            elif cmd == "rapoarte primii 30% clienti cu cele mei multe filme": self.__raport_primii_clienti_cu_cele_mai_inchiriate_filme()