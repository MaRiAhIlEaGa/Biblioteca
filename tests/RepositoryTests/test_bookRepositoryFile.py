from unittest import TestCase, mock

from Domain.carte import Carte
from Repository.bookRepositoryFile import BookRepositoryFile
from Repository.repository_exception import InexistentIDException, DuplicateIDException


class TestBookRepositoryFile(TestCase):
    def setUp(self) -> None:
        self.repository = BookRepositoryFile("carti.txt")
        self.carte = Carte(1, "Mara", "povesti", "Ioan Slavici")
        self.new_carte = Carte(2, "Baltagul", "roman", "Mihail Sadoveanu")

    def test_add(self):
        with self.assertRaises(DuplicateIDException):
            self.repository.add(self.carte)

    def test_modify(self):
        self.carte = self.repository.modify(self.new_carte)

    def test_delete(self):
        with self.assertRaises(InexistentIDException):
            self.repository.delete(self.carte.get_id())
            self.repository.delete(self.carte.get_id())

    def test_citeste_din_fisier(self):
        with self.assertRaises(DuplicateIDException):
            self.repository.add(self.carte)

    def test_scrie_in_fisier(self):
        with self.assertRaises(DuplicateIDException):
            self.repository.add(self.carte)
            self.repository.add(self.carte)

    def tearDown(self) -> None:  # metoda se executa DUPA fiecare test
        pass
