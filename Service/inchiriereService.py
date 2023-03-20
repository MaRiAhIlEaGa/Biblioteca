import operator

from Domain.inchiriere import Inchiriere


class InchiriereService:

    def __init__(self, inchiriere_repository, client_repository, book_repository):
        self.__inchiriere_repository = inchiriere_repository
        self.__client_repository = client_repository
        self.__book_repository = book_repository

    def get_all(self):
        return self.__inchiriere_repository.get_all()

    def add_inchiriere(self, id, book_id, client_id, carte):
        """Function that add a hire

        param id: id of the hire
        :param book_id: id of the book
        :param client_id: id of the client
        :param carte: the rented book
        """
        inchiriere = Inchiriere(id, book_id, client_id, carte)
        self.__inchiriere_repository.add(inchiriere)

    def sterge_inchirierea(self, id):
        """Delete the rental with the given id

        param id: id of the rental
        :return:
        """
        self.__inchiriere_repository.sterge_inchirieri_carte(id)
