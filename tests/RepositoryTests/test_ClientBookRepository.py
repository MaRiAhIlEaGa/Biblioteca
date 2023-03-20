from unittest import TestCase

from Domain.carte import Carte
from Domain.client import Client
from Domain.inchiriere import Inchiriere
from Repository.ClientBookRepository import ClientBookRepository, BookNrRepository
from Repository.bookRepository import BookRepository
from Repository.clientRepository import ClientRepository
from Repository.inchiriereRepository import InchiriereRepository
from Repository.repository import Repository


class TestClientBookRepository(TestCase):
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

    def test_save_c(self):
        self.assertIsNotNone(self.client_book_repository.create_dto_c())

    def test_save_b(self):
        self.assertIsNotNone(self.book_nr_repository.create_dto_b())
