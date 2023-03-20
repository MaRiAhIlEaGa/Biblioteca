from Domain.client import Client
from Repository.clientRepository import ClientRepository


class ClientRepositoryFile(ClientRepository):

    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.citeste_din_fisier()

    def add(self, client):
        """ The function that adds a client to the file

        param client: the client that will be added
        """
        super().add(client)
        self.scrie_in_fisier()

    def modify(self, new_client):
        """ The function that modify a client in file

        param new_client: the client that will be added in file
        """
        super().modify(new_client)
        self.scrie_in_fisier()

    def delete(self, idClient):
        """ The function that delete a client from file

        param idClient: id of the client that will be deleted
        """
        super().delete(idClient)
        self.scrie_in_fisier()

    def citeste_din_fisier(self):
        f = open(self.__file_name, "r")
        line = f.readline().strip("\n")
        while line != "":
            lista = line.split(",")
            id = int(lista[0])
            name = lista[1]
            CNP = lista[2]
            client = Client(id, name, CNP)
            super().add(client)
            line = f.readline().strip("\n")
        f.close()

    def scrie_in_fisier(self):
        f = open(self.__file_name, "w")
        clients_list = super().get_all()
        for client in clients_list:
            id = client.get_id()
            name = client.getName()
            CNP = client.getCNP()
            line = str(id) + "," + name + "," + CNP + "\n"
            f.write(line)
        f.close()
