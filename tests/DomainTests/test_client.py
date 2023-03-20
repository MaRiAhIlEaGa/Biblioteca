from unittest import TestCase

from Domain.client import Client


class TestClient(TestCase):
    def setUp(self) -> None:
        self.client = Client(1, "Maria", "1234")

    def test_get_name(self):
        self.assertEqual(self.client.getName(), "Maria")

    def test_get_cnp(self):
        self.assertEqual(self.client.getCNP(), "1234")

    def test_set_name(self):
        self.client.setName("Ana")
        self.assertEqual(self.client.Name, "Ana")

    def test_set_cnp(self):
        self.client.setCNP("22222")
        self.assertEqual(self.client.CNP, "22222")

    def test_str(self):
        self.assertTrue(self.client.__str__(), "Client " + str(
            self.client.get_id()) + ":\nNume: " + self.client.getName() + "\nCNP: " + self.client.getCNP() + "\n")

    def tearDown(self) -> None:  # metoda se executa DUPA fiecare test
        pass