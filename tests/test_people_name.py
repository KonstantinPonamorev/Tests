import unittest
from main import people_name



class TestPeopleName(unittest.TestCase):
    def setUp(self) -> None:
        print('Test starts')

    def tearDown(self) -> None:
        print('Test ends')

    def test_people_name_correct(self):
        self.assertEqual(people_name(10006), 1)

    def test_people_name_incorrect(self):
        self.assertEqual(people_name(100006), 0)

