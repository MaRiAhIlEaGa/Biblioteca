from Repository.repository_exception import *


class Menu:

    def __init__(self, bookService, clientService, inchirere_service, client_book_service):
        self.__bookService = bookService
        self.__clientService = clientService
        self.__inchirere_service = inchirere_service
        self.__client_book_service = client_book_service

    #                                       Books

    def ui_add_book(self):
        """Functia prin care se aduga o carte in lista
        """
        try:
            id_book = int(input("Introducteti id-ul cartii: "))
            title = input("Introdusceti titlul cartii: ")
            description = input("Introduceti o scurta descriere: ")
            author = input("Introduceti autorul cartii: ")
            self.__bookService.add_books(id_book, title, description, author)
        except DuplicateIDException as error:
            print(error)

    def ui_delete_book(self):
        '''Functia prin care se sterge o carte din lista
        '''
        try:
            id_book = int(input("Introduceti id-ul cartii care va fi stearsa: "))
            self.__bookService.delete_books(id_book)
        except InexistentIDException as error:
            print(error)

    def ui_modify_book(self):
        '''Functia prin care se modifica o carte din lista
        '''
        try:
            id_book = int(input("Intrduceti is-ul cartii care va fi modificata: "))
            new_title = input("Introduceti noul titlu: ")
            new_description = input("Introduceti o noua descriere: ")
            new_author = input("Introduceti un nou autor: ")
            self.__bookService.modify_books(id_book, new_title, new_description, new_author)
        except InexistentIDException as error:
            print(error)

    def ui_print_all_books(self):
        '''Functia care printeaza toate cartile din lista
        '''
        books = self.__bookService.get_all()
        if len(books) == 0:
            print("Lista nu contine nicio carte!")
        for book in books:
            print(book)

    def ui_get_book(self):
        id = int(input("Intrdoduceti id-ul cartii: "))
        all_books = self.__bookService.get_all()
        for book in all_books:
            if book.get_id() == id:
                print(book)

    def print_options_books(self):
        '''Functia care afisaza optiunile pentru gestiunea listei de carti
        '''
        print("1) Adaugare carte")
        print("2) Stergere carte")
        print("3) Modificare carte")
        print("4) Afisare lista de carti")
        print("5) Cautare carte")

    #                                    Clients

    def ui_add_clients(self):
        '''Functia prin care se aduga un client in lista
        '''
        try:
            id_client = int(input("Introducteti id-ul clientului: "))
            name = input("Introdusceti numele clientului: ")
            CNP = input("Introduceti CNP-ul clientului: ")
            self.__clientService.add_client(id_client, name, CNP)
        except DuplicateIDException as error:
            print(error)

    def ui_delete_client(self):
        '''Functia prin care se sterge un client din lista
        '''
        try:
            id_client = int(input("Introduceti is-ul clientului care va fi stears: "))
            self.__clientService.delete_client(id_client)
        except InexistentIDException as error:
            print(error)

    def ui_modify_client(self):
        '''Functia prin care se modifica un client din lista
        '''
        try:
            id_client = int(input("Intrduceti id-ul clientului care va fi modificat: "))
            new_name = input("Introduceti noul nume: ")
            new_CNP = input("Introduceti noul CNP: ")
            self.__clientService.modify_client(id_client, new_name, new_CNP)
        except InexistentIDException as error:
            print(error)

    def ui_print_all_clients(self):
        '''Functia care printeaza toti clientii din lista
        '''
        clients = self.__clientService.getAllClients()
        if len(clients) == 0:
            print("Lista nu contine niciun client!")
        for client in clients:
            print(client)

    @staticmethod
    def print_options_clients():
        '''Functia care afisaza optiunile pentru gestiunea listei de carti
        '''
        print("a) Adaugare client")
        print("b) Stergere client")
        print("c) Modificare client")
        print("d) Afisare lista de clienti")
        print("e) Cautare client")

    def ui_get_client(self):
        id = int(input("Intrdoduceti id-ul clientului: "))
        all_clients = self.__clientService.getAllClients()
        for client in all_clients:
            if client.get_id() == id:
                print(client)

    #                                                 Inchiriere/Returnare

    @staticmethod
    def print_options():
        print("1) Inchirere carte")
        print("2) Returnare carte")

    def ui_print_inchirere(self):
        inchirieri = self.__inchirere_service.get_all()
        if len(inchirieri) == 0:
            print("Lista de inchirieri e goala!")
        for inchiriere in inchirieri:
            print(inchiriere)

    def ui_add_inchiriere(self):
        try:
            id = int(input("Introduceti id: "))
            client_id = int(input("Introduceti ID client: "))
            book_id = int(input("Introduceti ID carte: "))
            carte = input("Introduceti cartea: ")
            self.__inchirere_service.add_inchiriere(id, book_id, client_id, carte)
        except ValueError:
            print("Date gresite! Reincercati!")
        except KeyError as ve:
            print(ve)

    def ui_cele_mai_inchiriate_carti(self):
        print(self.__client_book_service.cele_mai_inchiriate_carti())

    def ui_order_by_name(self):
        # carte = input("Introduceti numele cartii pentru care doriti sa ordonati alfabetic numele: ")
        print(self.__client_book_service.order_by_name())

    def ui_order_by_nr_books(self):
        print(self.__client_book_service.order_by_nr_carti())

    def ui_fist_20(self):
        print(self.__client_book_service.first_20())

    def ui_return_book(self):
        try:
            id = int(input("Introduceti id-ul imprumutului: "))
            self.__inchirere_service.sterge_inchirierea(id)
        except KeyError as ve:
            print(ve)

    #                                   Menu

    def menu(self):
        while True:
            opt = int(input("             BIBLIOTECA \n"
                            "Selecteaza o optiune:\n"
                            "     1) Gestiunea listei de carti\n"
                            "     2) Gestiunea listei de clienti\n"
                            "     3) Gestiune inchiriere/returnare\n"
                            "     4) Iesire\n"
                            ))
            if opt == 1:
                self.print_options_books()
            elif opt == 2:
                self.print_options_clients()
            elif opt == 3:
                self.print_options()
                opt_i = int(input())
                if opt_i == 1:
                    print("1.1) Adaugare inchiriere")
                    print("1.2) Tiparire inchirieri")
                    print("1.3) Clienți cu cărți închiriate ordonat dupa: nume")
                    print("1.4) Cele mai inchiriate carti")
                    print("1.5) Clienți cu cărți închiriate ordonat dupa: numărul de cărți închiriate")
                    print("1.6) Primii 20% cei mai activi clienti")
                else:
                    print("2.1) Returnare carte")
                    print("2.2) Tipareste lista imprumuturilor dupa returnare")
            else:
                break
            option = input()
            if option == "1":
                self.ui_add_book()
            elif option == "2":
                self.ui_delete_book()
            elif option == "3":
                self.ui_modify_book()
            elif option == "4":
                self.ui_print_all_books()
            elif option == "5":
                self.ui_get_book()
            elif option == "a":
                self.ui_add_clients()
            elif option == "b":
                self.ui_delete_client()
            elif option == "c":
                self.ui_modify_client()
            elif option == "d":
                self.ui_print_all_clients()
            elif option == "e":
                self.ui_get_client()
            elif option == "1.1":
                self.ui_add_inchiriere()
            elif option == "1.2":
                self.ui_print_inchirere()
            elif option == "1.3":
                self.ui_order_by_name()
            elif option == "1.4":
                self.ui_cele_mai_inchiriate_carti()
            elif option == "1.5":
                self.ui_order_by_nr_books()
            elif option == "1.6":
                self.ui_fist_20()
            elif option == "2.1":
                self.ui_return_book()
            elif option == "2.2":
                self.ui_print_inchirere()
            else:
                break
