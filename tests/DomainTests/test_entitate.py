from unittest import TestCase

from Domain.entitate import Entity


class TestEntity(TestCase):
    def setUp(self) -> None:
        self.entity = Entity(id=2)

    def test_get_id(self):
        self.assertEqual(self.entity.get_id(), 2)

    def test_set_id(self):
        self.entity.set_id(3)
        self.assertEqual(self.entity.get_id(), 3)

    def test_str(self):
        self.assertTrue(self.entity.__str__(), "ID: " + str(self.entity.get_id()) + "\n")

    def tearDown(self) -> None:  # metoda se executa DUPA fiecare test
        pass
