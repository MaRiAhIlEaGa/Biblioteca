from unittest import TestCase

from Domain.inchiriere import Inchiriere


class TestInchiriere(TestCase):
    def setUp(self) -> None:
        self.inchiriere = Inchiriere(1, 2, 3, "Mara")

    def test_get_id_book(self):
        self.assertEqual(self.inchiriere.get_id_book(), 2)

    def test_get_id_client(self):
        self.assertEqual(self.inchiriere.get_id_client(), 3)

    def test_get_book(self):
        self.assertEqual(self.inchiriere.get_book(), "Mara")

    def test_set_id_book(self):
        self.inchiriere.set_id_book(1)
        self.assertEqual(self.inchiriere.get_id_book(), 1)

    def test_set_id_client(self):
        self.inchiriere.set_id_client(1)
        self.assertEqual(self.inchiriere.get_id_client(), 1)

    def test_set_book(self):
        self.inchiriere.set_book("Baltagul")
        self.assertEqual(self.inchiriere.get_book(), "Baltagul")

    def test_str(self):
        self.assertTrue(self.inchiriere.__str__(), "Inchiriere: " + str(self.inchiriere.get_id()) + "\n" + \
                        "ID Client: " + str(self.inchiriere.get_id_client()) + "\n" + \
                        "ID Carte: " + str(self.inchiriere.get_id_book()) + "\n" + \
                        "Carte: " + self.inchiriere.get_book() + "\n")

    def tearDown(self) -> None:  # metoda se executa DUPA fiecare test
        pass
