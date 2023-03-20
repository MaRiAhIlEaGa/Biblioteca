class RepositoryException(Exception):

    def __init__(self, massage):
        self.__massage = massage

    def __str__(self):
        return self.__massage


class DuplicateIDException(RepositoryException):

    def __init__(self, massage):
        super().__init__(massage)


class InexistentIDException(RepositoryException):

    def __init__(self, massage):
        super().__init__(massage)
