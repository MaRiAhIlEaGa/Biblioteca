from dataclasses import dataclass


@dataclass
class ClientBookDTO:
    name: str
    nr_books: int


@dataclass
class BookNrDTO:
    name: str
    nr_inchirieri: int


class ClientBookDTOAssembler:
    @staticmethod
    def create_client_dto(client, inchirieri):
        name = client.getName()
        nr_books = 0
        for inchiriere in inchirieri:
            if client.get_id() == inchiriere.get_id_client():
                nr_books += 1
        return ClientBookDTO(name, nr_books)


class BookNrDTOAssembler:
    @staticmethod
    def create_book_dto(carte, inchirieri):
        name = carte.getName()
        nr_inchirieri = 0
        for inchiriere in inchirieri:
            if carte.get_id() == inchiriere.get_id_book():
                nr_inchirieri += 1
        return BookNrDTO(name, nr_inchirieri)
