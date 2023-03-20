from Repository.bookRepository import BookRepository
from Repository.clientRepository import ClientRepository
from Repository.repository import Repository
from Repository.repository_exception import InexistentIDException, DuplicateIDException


class InchiriereRepository(Repository):

    def __init__(self, book_repository, client_repository):
        super().__init__()
        self.__client_repository = client_repository
        self.__book_repository = book_repository

    def add_inchiriere(self, inchiriere):
        '''Functia prin care se adauga o inchiriere in lista de inchirieri

        :param inchiriere: inchirierea care va fi adaugata
        '''
        id = inchiriere.get_id()
        if self.gaseste_inchiriere_dupa_id(id) is not None:
            raise DuplicateIDException("Entitatea cu acest id exista!")
        else:
            client_id = inchiriere.get_id_client()
            book_id = inchiriere.get_id_book()
            if self.__client_repository.get_position_by_id(client_id) is None or \
                    self.__book_repository.get_position_by_id(book_id) is None:
                raise ValueError("Clientul sau cartea inscrierii nu exista!")
            elif self.gaseste_inchiriere_dupa_client_id_si_carte_id(client_id, book_id) is not None:
                raise ValueError("Clientul a inchiriat deja aceasta carte!")
            else:
                self._lista.append(inchiriere)

    def gaseste_inchiriere_dupa_id(self, id):
        '''
        Metoda care gaseste o inscriere in lista de inscrieri, dupa id inscriere
        :param id: id-ul inscrierii cautate
        '''
        for i in range(0, len(self._lista)):
            inchiriere = self._lista[i]
            if inchiriere.get_id() == id:
                return i
        return None

    def gaseste_inchiriere_dupa_client_id_si_carte_id(self, client_id, book_id):
        '''
        Functia care gaseste o inchiriere in lista de inchirieri, dupa id client si id carte
        :param book_id:
        :param client_id:
        '''
        for i in range(0, len(self._lista)):
            inchiriere = self._lista[i]
            if inchiriere.get_id_client() == client_id and inchiriere.get_id_book() == book_id:
                return i
        return None

    def sterge_inchirieri_carte(self, id):
        '''Functie prin care se sterge o inchiriere

        :param id: id ul inchirierii care va fi steasta
        '''
        if self.gaseste_inchiriere_dupa_id(id) is None:
            raise InexistentIDException("Entitatea cu acest id nu exista!")
        else:
            index = self.gaseste_inchiriere_dupa_id(id)
            self._lista.pop(index)

