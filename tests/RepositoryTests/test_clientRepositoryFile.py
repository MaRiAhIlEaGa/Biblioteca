from unittest import TestCase

from Domain.client import Client
from Repository.clientRepositoryFile import ClientRepositoryFile
from Repository.repository_exception import DuplicateIDException, InexistentIDException


class TestClientRepositoryFile(TestCase):
    def setUp(self) -> None:
        self.repository = ClientRepositoryFile("clienti.txt")
        self.client = Client(1, "Maria", "11111")
        self.new_client = Client(2, "Diana", "22222")

    def test_add(self):
        with self.assertRaises(DuplicateIDException):
            self.repository.add(self.client)

    def test_modify(self):
        new_client = Client(5, "Ana", "3333")
        with self.assertRaises(InexistentIDException):
            self.repository.modify(new_client)
        test_client = Client(4, "aaa", "1111")
        with self.assertRaises(DuplicateIDException):
            self.repository.add(test_client)
        new_test_client = Client(4, "bbb", "2222")
        self.repository.modify(new_test_client)

    def test_delete(self):
        with self.assertRaises(InexistentIDException):
            self.repository.delete(self.client.get_id())
            self.repository.delete(self.client.get_id())

    def test_citeste_din_fisier(self):
        with self.assertRaises(InexistentIDException):
            self.client = self.repository.modify(self.new_client)
        self.assertEqual(self.client.Name, "Maria")

    def test_scrie_in_fisier(self):
        with self.assertRaises(DuplicateIDException):
            self.repository.add(self.client)
            self.repository.add(self.client)
        with open("clienti.txt", "r") as file:
            content = file.read()
        self.assertIsNotNone(content)

    def tearDown(self) -> None:  # metoda se executa DUPA fiecare test
        pass

