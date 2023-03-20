from unittest import TestCase
from Domain.carte import Carte
from Repository.bookRepository import BookRepository
from Service.bookService import BookService


class TestBookService(TestCase):
    def setUp(self) -> None:
        self.book_repository = BookRepository()
        self.__repository = BookService(self.book_repository)
        self.carte1 = Carte(1, "Mara", "povesti", "Ioan Slavici")
        self.carte2 = Carte(2, "Baltagul", "roman", "Mihail Sadoveanu")
        self.__repository.add_books(1, "Mara", "povesti", "Ioan Slavici")
        self.__repository.add_books(2, "Baltagul", "roman", "Mihail Sadoveanu")

    def test_get_all_books(self):
        l = self.__repository.get_all()
        self.assertEqual(len(l), 2)

    def test_get_book_name(self):
        name = self.__repository.get_book_name(self.carte1)
        self.assertIsNone(name)

    def test_add_books(self):
        l = self.__repository.get_all()
        self.assertEqual(len(l), 2)

    def test_modify_books(self):
        l = self.__repository.get_all()
        self.carte1 = self.__repository.modify_books(1, "Ion", "roman", "Liviu Rebreanu")
        self.assertIsNot(l[0], self.carte1)

    def test_delete_books(self):
        l = self.__repository.get_all()
        self.__repository.delete_books(1)
        self.assertEqual(len(l), 1)
