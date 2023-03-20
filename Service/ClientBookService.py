class ClientBookService:
    def __init__(self, client_book_repository, book_nr_repository):
        self.client_book_repository = client_book_repository
        self.book_nr_repository = book_nr_repository

    def get_all(self):
        return self.client_book_repository.save_c()

    def cele_mai_inchiriate_carti(self):
        """Function that returns a list of the most rented books

        :return: a list of the most rented books
        """
        all_book_hire = self.book_nr_repository.create_dto_b()
        all_book_hire = sorted(all_book_hire, key=lambda x: x.nr_inchirieri, reverse=True)
        return all_book_hire[:1]

    def order_by_name(self):
        """ Function that return a list with rentals ordered by name

        :return: a list with rentals ordered by name
        """
        self.client_book_repository.clear_list()
        all_client_book = self.client_book_repository.create_dto_c()
        all_client_book = sorted(all_client_book, key=lambda x: x.name, reverse=False)
        return all_client_book

    def order_by_nr_carti(self):
        """ Function that return a list with rentals ordered by number of books

        :return: a list with rentals ordered by number of books
        """
        self.client_book_repository.clear_list()
        all_client_book = self.client_book_repository.create_dto_c()
        new_dic = sorted(all_client_book, key=lambda x: x.nr_books, reverse=True)
        return new_dic

    def first_20(self):
        """ Function that return a list with first 20 the most active clients

        :return: a list with first 20 the most active clients
        """
        self.client_book_repository.clear_list()
        all_client_book = self.client_book_repository.create_dto_c()
        all_client_book = sorted(all_client_book, key=lambda x: x.nr_books, reverse=True)
        lung = int(20//100 * len(all_client_book)) + 1
        return all_client_book[:lung]
