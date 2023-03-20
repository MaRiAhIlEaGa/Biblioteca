from Domain.entitate import Entity


class Carte(Entity):

    def __init__(self, idBook, title, description, author):
        super().__init__(idBook)
        self.title = title
        self.description = description
        self.author = author

    def getName(self):
        return self.title

    def getDescription(self):
        return self.description

    def getAuthor(self):
        return self.author

    def setTitle(self, new_title):
        self.title = new_title

    def setDescription(self, new_description):
        self.description = new_description

    def setAuthor(self, new_author):
        self.author = new_author

    def __str__(self):
        return "Carte " + str(self.get_id()) + " :" + "\n" + "Titlu: " + self.getName() + "\n" + "Descriere: " + \
               self.getDescription() + "\n" + "Autor: " + self.getAuthor()
