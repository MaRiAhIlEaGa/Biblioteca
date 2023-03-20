from Repository.repository import Repository


class BookRepository(Repository):
    
    def __init__(self):
        super().__init__()

    def get_book_name(self, id_book):
        """Functia prin care se preia titlul unei carti

        :param id_book:
        :return: titlul cartii
        """
        for i in range(0, len(self._lista)):
            current_book = self._lista[i]
            if id_book == current_book.get_id():
                return current_book.getName()
        return None
