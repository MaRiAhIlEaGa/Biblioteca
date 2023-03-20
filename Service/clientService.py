from Domain.client import Client


class ClientService:

    def __init__(self, repository):
        self.__repository = repository

    def getAllClients(self):
        '''Functia returneaza lista de clienti din clientRepository

        :return: lista de clienti
        '''
        return self.__repository.get_all()

    def add_client(self, idClient, name, CNP):
        '''Functia prin care se adauga un client in lista

        :param idClient: id client
        :param name: nume client
        :param CNP: CNP client
        '''
        client = Client(idClient, name, CNP)
        self.__repository.add(client)

    def modify_client(self, id_client, new_name, new_CNP):
        ''' Functia prin care se modifica un client din lsita

        :param id_client: id-ul clientului care va fi modificat
        :param new_name:  noul nume
        :param new_CNP: noul CNP
        '''
        client = Client(id_client, new_name, new_CNP)
        self.__repository.modify(client)

    def delete_client(self, idClient):
        '''Functia sterge o carte din lista

        :param idBook: id-ul cartii care va fi stearsa
        '''
        self.__repository.delete(idClient)

