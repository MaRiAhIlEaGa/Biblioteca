from unittest import TestCase

from Domain.entitate import Entity
from Repository.repository import Repository
from Repository.repository_exception import InexistentIDException, DuplicateIDException


class TestRepository(TestCase):
    def setUp(self) -> None:
        self.lista = []
        self.entity1 = Entity(1)
        self.entity2 = Entity(2)
        self.entity3 = Entity(3)
        self.repository = Repository()

    def test_get_all(self):
        self.repository.add(self.entity1)
        self.repository.add(self.entity2)
        l = self.repository.get_all()
        self.assertEqual(l[0], self.entity1)
        self.assertEqual(l[1], self.entity2)

    def test_add(self):
        self.repository.add(self.entity1)
        l = self.repository.get_all()
        self.assertEqual(l[0], self.entity1)

    def test_modify(self):
        try:
            self.repository.add(self.entity1)
            l = self.repository.get_all()
            self.assertEqual(l[0], self.entity1)
            self.entity1 = self.repository.modify(self.entity2)
            # self.assertIn(self.entity2, l)
        except InexistentIDException as error:
            print(error)

    def test_delete(self):
        try:
            self.repository.add(self.entity1)
            l = self.repository.get_all()
            self.assertEqual(l[0], self.entity1)
            self.repository.delete(self.entity1)
            # self.assertEqual(len(l), 0)
        except InexistentIDException as error:
            print(error)

    def test_get_position_by_id(self):
        self.repository.add(self.entity1)
        poz = self.repository.get_position_by_id(self.entity1.get_id())
        self.assertEqual(poz, 0)

    def test_get_entity_by_id(self):
        entity = self.repository.get_entity_by_id(self.entity1.get_id())
        self.assertIsNone(entity)
        self.repository.add(self.entity1)
        entity = self.repository.get_entity_by_id(self.entity1.get_id())
        self.assertIsNotNone(entity)
