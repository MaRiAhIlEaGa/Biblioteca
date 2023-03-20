from unittest import TestCase

from Domain.carte import Carte
from Domain.client import Client
from Domain.dto import ClientBookDTO, ClientBookDTOAssembler, BookNrDTOAssembler, BookNrDTO
from Domain.inchiriere import Inchiriere
from Repository.bookRepository import BookRepository
from Repository.clientRepository import ClientRepository
from Repository.inchiriereRepository import InchiriereRepository
from Repository.repository import Repository


class TestClientBookDTOAssembler(TestCase):
    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.ClientBookDTO = None

    def setUp(self) -> None:
        self.nr_book = 0
        self.dto_book = BookNrDTO("Mara", 3)
        self.dto_client = ClientBookDTO("Maria", 3)
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
        self.inchirieri = self.inchiriere_repository.get_all()

    def test_create_client_dto(self):
        self.assertEqual(self.dto_client.name, "Maria")
        self.assertEqual(self.dto_client.nr_books, 3)
        self.assertEqual(self.client.getName(), "Maria")
        ClientBookDTOAssembler.create_client_dto(self.client, self.inchirieri)
        self.assertIsNotNone(self.dto_client.nr_books)

    def test_create_book_dto(self):
        self.assertEqual(self.dto_book.name, "Mara")
        self.assertEqual(self.dto_book.nr_inchirieri, 3)
        self.assertEqual(self.carte.getName(), "Mara")
        BookNrDTOAssembler.create_book_dto(self.carte, self.inchirieri)
        self.assertIsNotNone(self.dto_book.nr_inchirieri)
