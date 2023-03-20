import operator
from unittest import TestCase

from Domain.carte import Carte
from Domain.client import Client
from Domain.inchiriere import Inchiriere
from Repository.bookRepository import BookRepository
from Repository.clientRepository import ClientRepository
from Repository.inchiriereRepository import InchiriereRepository
from Service.inchiriereService import InchiriereService


class TestInchiriereService(TestCase):
    def setUp(self) -> None:
        self.client_repository = ClientRepository()
        self.book_repository = BookRepository()
        self.inchiriere_repository = InchiriereRepository(self.book_repository, self.client_repository)
        self.inchiriere_service = InchiriereService(self.inchiriere_repository, self.client_repository,
                                                    self.book_repository)
        self.carte1 = Carte(1, "Mara", "povesti", "Ioan Slavici")
        self.carte2 = Carte(2, "Baltagul", "roman", "Mihail Sadoveanu")
        self.book_repository.add(self.carte1)
        self.book_repository.add(self.carte2)
        self.client1 = Client(1, "Maria", "11111")
        self.client2 = Client(2, "Diana", "22222")
        self.client_repository.add(self.client1)
        self.client_repository.add(self.client2)

    def test_get_all(self):
        inchirieri = self.inchiriere_service.get_all()
        self.assertEqual(inchirieri, [])
        self.inchiriere_service.add_inchiriere(1, 1, 1, "Mara")
        inchirieri = self.inchiriere_service.get_all()
        self.assertEqual(len(inchirieri), 1)

    def test_add_inchiriere(self):
        self.inchiriere_service.add_inchiriere(1, 1, 1, "Mara")
        inchirieri = self.inchiriere_service.get_all()
        self.assertEqual(len(inchirieri), 1)

    def test_sterge_inchirierea(self):
        self.inchiriere_service.add_inchiriere(1, 1, 1, "Mara")
        inchirieri = self.inchiriere_service.get_all()
        self.assertEqual(len(inchirieri), 1)
        self.inchiriere_service.sterge_inchirierea(1)
        inchirieri = self.inchiriere_service.get_all()
        self.assertEqual(len(inchirieri), 0)

    # def test_cele_mai_inchiriate_carti(self):
    #     self.inchiriere_service.add_inchiriere(1, 1, 1, "Mara")
    #     self.inchiriere_service.add_inchiriere(2, 1, 2, "Mara")
    #     self.assertIsNone(self.book_repository.get_book_name(3))
    #     dic = self.inchiriere_service.cele_mai_inchiriate_carti()
    #     self.assertEqual(dic, self.carte1)
    #
    # def test_return_client_order_by_name(self):
    #     self.assertRaises(ValueError, self.inchiriere_service.return_client_order_by_name, "None")
    #     self.inchiriere_service.add_inchiriere(1, 1, 1, "Mara")
    #     self.inchiriere_service.add_inchiriere(2, 1, 2, "Mara")
    #     self.assertIsNone(self.book_repository.get_book_name(3))
    #     dic = self.inchiriere_service.return_client_order_by_name("Mara")
    #     self.assertIn("Diana", dic)
    #
    # def test_get_clienti_carte(self):
    #     self.inchiriere_service.add_inchiriere(1, 1, 1, "Mara")
    #     self.inchiriere_service.add_inchiriere(2, 1, 2, "Mara")
    #     books = self.book_repository.get_all()
    #     doc = {}
    #     for book in books:
    #         doc[book] = len(self.inchiriere_service.get_clienti_carte(book.get_id()))
    #     self.assertEqual(max(doc.items(), key=operator.itemgetter(1))[0], self.carte1)
    #
    # def test_get_nr_carti(self):
    #     self.inchiriere_service.add_inchiriere(1, 1, 1, "Mara")
    #     nr_carti = self.inchiriere_service.get_nr_carti(1)
    #     self.assertEqual(nr_carti, 1)
    #
    # def test_get_client_nr_carti(self):
    #     self.inchiriere_service.add_inchiriere(1, 1, 1, "Mara")
    #     self.inchiriere_service.add_inchiriere(2, 1, 2, "Mara")
    #     doc = self.inchiriere_service.get_client_nr_carti()
    #     self.assertEqual(doc["Maria"], 1)
    #
    # def test_first_20(self):
    #     self.inchiriere_service.add_inchiriere(1, 1, 1, "Mara")
    #     self.inchiriere_service.add_inchiriere(2, 1, 2, "Mara")
    #     self.inchiriere_service.add_inchiriere(3, 2, 1, "Baltagul")
    #     client3 = Client(3, "Marcello", "3333")
    #     client4 = Client(4, "Dani", "5555")
    #     client5 = Client(5, "Cori", "66666")
    #     self.client_repository.add(client3)
    #     self.client_repository.add(client4)
    #     self.client_repository.add(client5)
    #     self.inchiriere_service.add_inchiriere(4, 1, 3, "Mara")
    #     self.inchiriere_service.add_inchiriere(5, 1, 4, "Mara")
    #     self.inchiriere_service.add_inchiriere(6, 1, 5, "Mara")
    #     docs = self.inchiriere_service.first_20()
    #     self.assertIsNot(docs, {})
