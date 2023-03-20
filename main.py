from Repository.ClientBookRepository import ClientBookRepository, BookNrRepository
from Repository.bookRepositoryFile import BookRepositoryFile
from Repository.clientRepositoryFile import ClientRepositoryFile
from Repository.inchiriereRepositoryFile import InchiriereRepositoryFile
from Service.ClientBookService import ClientBookService
from Service.inchiriereService import InchiriereService
from UI.ui import Menu
from Service.bookService import BookService
from Service.clientService import ClientService

book_repository = BookRepositoryFile("carti.txt")
client_repository = ClientRepositoryFile("clienti.txt")
inchiriere_repository = InchiriereRepositoryFile("inchirieri.txt", client_repository, book_repository)
client_book_repository = ClientBookRepository(client_repository, inchiriere_repository)
book_nr_repository = BookNrRepository(book_repository, inchiriere_repository)
book_service = BookService(book_repository)
client_service = ClientService(client_repository)
inchiriere_service = InchiriereService(inchiriere_repository, client_repository, book_repository)
client_book_service = ClientBookService(client_book_repository, book_nr_repository)

menu = Menu(book_service, client_service, inchiriere_service, client_book_service)

menu.menu()
