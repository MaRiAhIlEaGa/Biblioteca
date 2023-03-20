from unittest import TestCase

from Domain.carte import Carte
from Domain.client import Client
from Domain.inchiriere import Inchiriere
from Repository.bookRepository import BookRepository
from Repository.clientRepository import ClientRepository
from Repository.inchiriereRepositoryFile import InchiriereRepositoryFile
from Repository.repository_exception import DuplicateIDException, InexistentIDException


class TestInchiriereRepositoryFile(TestCase):
    def setUp(self) -> None:
        self.client_repository = ClientRepository()
        self.book_repository = BookRepository()
        self.repository = InchiriereRepositoryFile("inchirieri.txt", self.client_repository, self.book_repository)
        self.carte = Carte(1, "Mara", "povesti", "Ioan Slavici")
        self.client1 = Client(1, "Maria", "11111")
        self.client2 = Client(2, "Diana", "22222")
        self.inchiriere = Inchiriere(1, 1, 1, "Mara")
        self.new_inchiriere = Inchiriere(2, 1, 2, "Mara")

    def test_add(self):
        with self.assertRaises(DuplicateIDException):
            self.repository.add(self.inchiriere)

    def test_modify(self):
        with self.assertRaises(InexistentIDException):
            self.inchiriere = self.repository.modify(self.new_inchiriere)

    def test_delete(self):
        with self.assertRaises(InexistentIDException):
            self.repository.delete(self.inchiriere.get_id())
            self.repository.delete(self.inchiriere.get_id())

    def test_citeste_din_fisier(self):
        with self.assertRaises(DuplicateIDException):
            self.repository.add(self.inchiriere)

    def test_scrie_in_fisier(self):
        with self.assertRaises(DuplicateIDException):
            self.repository.add(self.inchiriere)
            self.repository.add(self.inchiriere)

    def tearDown(self) -> None:  # metoda se executa DUPA fiecare test
        pass
