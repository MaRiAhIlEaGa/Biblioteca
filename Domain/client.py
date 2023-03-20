from Domain.entitate import Entity


class Client(Entity):

    def __init__(self, idClient, Name, CNP):
        super().__init__(idClient)
        self.Name = Name
        self.CNP = CNP

    def getName(self):
        return self.Name

    def getCNP(self):
        return self.CNP

    def setName(self, new_name):
        self.Name = new_name

    def setCNP(self, new_CNP):
        self.CNP = new_CNP

    def __str__(self):
        return "Client " + str(self.get_id()) + " :" + "\n" + "Nume: " + self.getName() + "\n" + "CNP: " + \
               self.getCNP()
