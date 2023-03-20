from Domain.carte import Carte
from Repository.bookRepository import BookRepository
from Repository.repository import Repository


class BookService:
    def __init__(self, repository: Repository):
        self.__repository = repository
        self.__book_repository = BookRepository()

    def get_all(self) -> object:
        '''Functia returneaza lista de carti din bookRepository

        :return: lista de carti
        '''
        return self.__repository.get_all()

    def get_book_name(self, id_book):
        return self.__book_repository.get_book_name(id_book)

    def add_books(self, idBook, title, description, author):
        ''' Functia prin care se adauga o carte in lsita
        :param idBook: id-ul cartii
        :param title: titlul cartii
        :param description: descrierea cartii
        :param author: autorul cartii
        '''
        book = Carte(idBook, title, description, author)
        self.__repository.add(book)

    def modify_books(self, idBook, new_title, new_description, new_author):
        ''' Functia prin care se modifica o carte din lsita
        :param idBook: id-ul cartii
        :param new_title: titlul cartii
        :param new_description: descrierea cartii
        :param new_author: autorul cartii
        '''
        new_book = Carte(idBook, new_title, new_description, new_author)
        self.__repository.modify(new_book)

    def delete_books(self, idBook):
        '''Functia sterge o carte din lista

        :param idBook: id-ul cartii care va fi stearsa
        '''
        self.__repository.delete(idBook)
