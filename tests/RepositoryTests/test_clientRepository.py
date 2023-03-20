from unittest import TestCase

from Domain.client import Client
from Repository.clientRepository import ClientRepository


class TestClientRepository(TestCase):
    def setUp(self) -> None:
        self.client_repository = ClientRepository()
        self.clients = self.client_repository.get_all()
        self.client = Client(1, "Maria", "1234")

    def test_get_client_name(self):
        self.assertIsNone(self.client_repository.get_client_name(self.client.get_id()))
        self.clients = self.client_repository.add(self.client)
        client_name = self.client_repository.get_client_name(self.client.get_id())
        self.assertEqual(client_name, "Maria")
