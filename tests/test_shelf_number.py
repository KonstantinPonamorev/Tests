import unittest
from main import shelf_number



class TestShelfNumber(unittest.TestCase):
    def setUp(self) -> None:
        print('Test starts')

    def tearDown(self) -> None:
        print('Test ends')

    def test_shelf_number_correct(self):
        self.assertNotEqual(shelf_number('11-2'), 0)

    def test_shelf_number_incorrect(self):
        self.assertNotEqual(shelf_number('112'), 1)
