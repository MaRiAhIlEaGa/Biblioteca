from unittest import TestCase

from Domain.client import Client
from Repository.clientRepository import ClientRepository
from Service.clientService import ClientService


class TestClientService(TestCase):
    def setUp(self) -> None:
        self.client_repository = ClientRepository()
        self.__repository = ClientService(self.client_repository)
        self.client1 = Client(1, "Maria", "1234")
        self.client2 = Client(2, "Marcello", "2345")
        self.__repository.add_client(1, "Maria", "1234")
        self.__repository.add_client(2, "Marcello", "2345")

    def test_get_all_clients(self):
        l = self.__repository.getAllClients()
        self.assertEqual(len(l), 2)

    def test_add_client(self):
        l = self.__repository.getAllClients()
        self.assertEqual(len(l), 2)

    def test_modify_client(self):
        l = self.__repository.getAllClients()
        self.client1 = self.__repository.modify_client(1, "Diana", "11111")
        self.assertIsNot(l[0], self.client1)

    def test_delete_client(self):
        l = self.__repository.getAllClients()
        self.__repository.delete_client(1)
        self.assertEqual(len(l), 1)
