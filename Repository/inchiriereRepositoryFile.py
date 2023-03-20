from Domain.inchiriere import Inchiriere
from Repository.inchiriereRepository import InchiriereRepository


class InchiriereRepositoryFile(InchiriereRepository):

    def __init__(self, file_name, client_repository, inchiriere_repository):
        super().__init__(client_repository, inchiriere_repository)
        self.__file_name = file_name
        self.citeste_din_fisier()

    def add(self, inchiriere):
        """ The function that adds a hire to the file

        param inchiriere: the hire that will be added
        """
        super().add(inchiriere)
        self.scrie_in_fisier()

    def delete(self, id):
        """ The function that delete a hire from file

        param id: id of the hire that will be deleted
        """
        super().sterge_inchirieri_carte(id)
        self.scrie_in_fisier()

    def citeste_din_fisier(self):
        f = open(self.__file_name, "r")
        line = f.readline().strip("\n")
        while line != "":
            lista = line.split(",")
            id = int(lista[0])
            id_client = int(lista[1])
            id_carte = int(lista[2])
            carte = lista[3]
            inchirere = Inchiriere(id, id_carte, id_client, carte)
            super().add(inchirere)
            line = f.readline().strip("\n")
        f.close()

    def scrie_in_fisier(self):
        f = open(self.__file_name, "w")
        inchirieri_list = super().get_all()
        for inchiriere in inchirieri_list:
            id = inchiriere.get_id()
            id_client = inchiriere.get_id_client()
            id_carte = inchiriere.get_id_book()
            carte = inchiriere.get_book()
            line = str(id) + "," + str(id_client) + "," + str(id_carte) + "," + carte + "\n"
            f.write(line)
        f.close()