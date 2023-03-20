from Domain.carte import Carte
from Repository.bookRepository import BookRepository


class BookRepositoryFile(BookRepository):

    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.citeste_din_fisier()

    def add(self, book):
        """ The function that adds a book to the file

        param book: the book that will be added
        """
        super().add(book)
        self.scrie_in_fisier()

    def modify(self, new_book):
        """ The function that modify a book in file

        param new_book: the book that will be added in file
        """
        super().modify(new_book)
        self.scrie_in_fisier()

    def delete(self, idBook):
        """ The function that delete a book from file

        param idBook: id of the book that will be deleted
        """
        super().delete(idBook)
        self.scrie_in_fisier()

    def citeste_din_fisier(self):
        f = open(self.__file_name, "r")
        line = f.readline().strip("\n")
        while line != "":
            lista = line.split(",")
            id = int(lista[0])
            title = lista[1]
            description = lista[2]
            author = lista[3]
            book = Carte(id, title, description, author)
            super().add(book)
            line = f.readline().strip("\n")
        f.close()

    def scrie_in_fisier(self):
        f = open(self.__file_name, "w")
        book_list = super().get_all()
        for book in book_list:
            id = book.get_id()
            title = book.getName()
            description = book.getDescription()
            author = book.getAuthor()
            line = str(id) + "," + title + "," + description + "," + author + "\n"
            f.write(line)
        f.close()