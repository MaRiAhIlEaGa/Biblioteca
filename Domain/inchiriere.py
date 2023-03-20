from Domain.entitate import Entity


class Inchiriere(Entity):

    def __init__(self, id, idBook, idClient, Carte):
        super().__init__(id)
        self.__idBook = idBook
        self.__idClient = idClient
        self.__carte = Carte

    def get_id_book(self):
        return self.__idBook

    def get_id_client(self):
        return self.__idClient

    def get_book(self):
        return self.__carte

    def set_id_book(self, new_id):
        self.__idBook = new_id

    def set_id_client(self, new_id):
        self.__idClient = new_id

    def set_book(self, new_book):
        self.__carte = new_book

    def __str__(self):
        return "Inchiriere: " + str(self.get_id()) + "\n" + \
               "ID Client: " + str(self.get_id_client()) + "\n" + \
               "ID Carte: " + str(self.get_id_book()) + "\n" + \
               "Carte: " + self.get_book() + "\n"
