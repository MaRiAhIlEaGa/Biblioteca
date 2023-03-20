from unittest import TestCase
from Domain.carte import Carte


class TestCarte(TestCase):
    def setUp(self) -> None:
        self.carte = Carte(1, "Mara", "povesti", "Ioan Slavici")

    def test_get_title(self):
        self.assertEqual(self.carte.getName(), "Mara")

    def test_get_description(self):
        self.assertEqual(self.carte.getDescription(), "povesti")

    def test_get_author(self):
        self.assertEqual(self.carte.getAuthor(), "Ioan Slavici")

    def test_set_title(self):
        self.carte.setTitle("Baltagul")
        self.assertEqual(self.carte.title, "Baltagul")

    def test_set_description(self):
        self.carte.setDescription("roman")
        self.assertEqual(self.carte.description, "roman")

    def test_set_author(self):
        self.carte.setAuthor("Mihail Sadoveanu")
        self.assertEqual(self.carte.author, "Mihail Sadoveanu")

    def test_str(self):
        self.assertTrue(self.carte.__str__(), "Carte " + str(
            self.carte.get_id()) + ":\nTitlu: " + self.carte.getName() + "\nDescriere: " + self.carte.getDescription()
                        + "\nAutor: " + self.carte.getAuthor() + "\n")

    def tearDown(self) -> None:  # metoda se executa DUPA fiecare test
        pass
