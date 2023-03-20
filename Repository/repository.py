from Repository.repository_exception import DuplicateIDException, InexistentIDException


class Repository:

    def __init__(self):
        self._lista = []

    def get_all(self):
        '''
        Metoda care returneaza lista de entitati
        :return:
        '''
        return self._lista

    def add(self, entity):
        '''
        Metoda care adauga o entitate in lista
        :param entity:
        :return:
        '''
        if self.get_position_by_id(entity.get_id()) is not None:
            raise DuplicateIDException("Exista deja o entitate cu acest id!")
        else:
            self._lista.append(entity)

    def modify(self, new_entity):
        '''
        Metoda care modifica o entitate existenta
        :param new_entity:
        :return:
        '''
        id_new_entity = new_entity.get_id()
        if self.get_position_by_id(id_new_entity) is None:
            raise InexistentIDException("Entitatea cu acest id nu exista!")
        else:
            index = self.get_position_by_id(id_new_entity)
            self._lista[index] = new_entity

    def delete(self, id):
        '''
        Metoda care sterge din lista o entitate dupa id
        :param id:
        :return:
        '''
        if self.get_position_by_id(id) is None:
            raise InexistentIDException("Entitatea cu acest id nu exista!")
        else:
            index = self.get_position_by_id(id)
            self._lista.pop(index)

    def get_position_by_id(self, id):
        '''
        Metoda care returneaza pozitia in lista a unei entitati, dupa id
        :param id:
        :return: pozitia entitatii in lista, daca ea exista; -1, altfel
        '''
        for i in range(0, len(self._lista)):
            current_entity = self._lista[i]
            if current_entity.get_id() == id:
                return i
        return None

    def get_entity_by_id(self, id):
        '''
        Metoda ce returneaza entitatea dupa id-ul dat
        :param id:
        :return: entitatea cu id-ul dat, daca ea exista; -1 altfel
        '''
        for i in range(0, len(self._lista)):
            current_entity = self._lista[i]
            if current_entity.get_id() == id:
                return current_entity
        return None
