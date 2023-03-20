from Domain.dto import ClientBookDTOAssembler, BookNrDTOAssembler


class ClientBookRepository:
    def __init__(self, client_repository, inchiriere_repository):
        self.client_repository = client_repository
        self.inchiriere_repository = inchiriere_repository
        self.all_client_books = []

    def save_c(self):
        """ The function that creates a list of entities

         :return: a list of entities
         """
        clients = self.client_repository.get_all()
        inchirieri = self.inchiriere_repository.get_all()
        for client in clients:
            self.all_client_books.append(ClientBookDTOAssembler.create_client_dto(client, inchirieri))
        return self.all_client_books

    def create_dto_c(self):
        """ The function that return a list of entities

               :return: a list of entities
               """
        return list(self.save_c())

    def clear_list(self):
        self.all_client_books.clear()


class BookNrRepository:
    def __init__(self, book_repository, inchiriere_repository):
        self.book_repository = book_repository
        self.inchiriere_repository = inchiriere_repository
        self.all_books_hire = []

    def save_b(self):
        """ The function that creates a list of entities

        :return: a list of entities
        """
        books = self.book_repository.get_all()
        inchirieri = self.inchiriere_repository.get_all()
        for books in books:
            self.all_books_hire.append(BookNrDTOAssembler.create_book_dto(books, inchirieri))
        return self.all_books_hire

    def create_dto_b(self):
        """ The function that return a list of entities

        :return: a list of entities
        """
        return list(self.save_b())