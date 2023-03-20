from unittest import TestCase
from Domain.carte import Carte
from Repository.bookRepository import BookRepository


class TestBookRepository(TestCase):
    def setUp(self) -> None:
        self.book_repository = BookRepository()
        self.books = self.book_repository.get_all()
        self.book = Carte(1, "Mara", "povesti", "Ioan Slavici")

    def test_get_book_name(self):
        self.assertIsNone(self.book_repository.get_book_name(self.book.get_id()))
        self.books.append(self.book)
        title = self.book.title
        title_book = self.book_repository.get_book_name(self.book.get_id())
        self.assertIs(title_book, title)
