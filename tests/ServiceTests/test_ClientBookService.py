from unittest import TestCase

from Domain.carte import Carte
from Domain.client import Client
from Domain.inchiriere import Inchiriere
from Repository.ClientBookRepository import ClientBookRepository, BookNrRepository
from Repository.bookRepository import BookRepository
from Repository.clientRepository import ClientRepository
from Repository.inchiriereRepository import InchiriereRepository
from Repository.repository import Repository
from Service.ClientBookService import ClientBookService


class TestClientBookService(TestCase):
    def setUp(self) -> None:
        self.client = Client(1, "Maria", "1111")
        self.carte = Carte(1, "Mara", "povesti", "Ioan Slavici")
        self.inchiriere = Inchiriere(1, 1, 1, "Mara")
        self.repository = Repository()
        self.book_repository = BookRepository()
        self.book_repository.add(self.carte)
        self.client_repository = ClientRepository()
        self.client_repository.add(self.client)
        self.inchiriere_repository = InchiriereRepository(self.book_repository, self.client_repository)
        self.inchiriere_repository.add_inchiriere(self.inchiriere)
        self.client_book_repository = ClientBookRepository(self.client_repository, self.inchiriere_repository)
        self.book_nr_repository = BookNrRepository(self.book_repository, self.inchiriere_repository)
        self.client_book_service = ClientBookService(self.client_book_repository, self.book_nr_repository)
        self.all_dto = self.client_book_service.get_all()

    def test_get_all(self):
        self.assertIsNotNone(self.all_dto)

    def test_cele_mai_inchiriate_carti(self):
        obj = self.client_book_service.cele_mai_inchiriate_carti()
        self.assertIsNotNone(obj)

    def test_order_by_name(self):
        dic = self.client_book_service.order_by_name()
        self.assertIsNotNone(dic)

    def test_order_by_nr_carti(self):
        dic = self.client_book_service.order_by_nr_carti()
        self.assertIsNotNone(dic)

    def test_first_20(self):
        dic = self.client_book_service.first_20()
        self.assertIsNotNone(dic)
