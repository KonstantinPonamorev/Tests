import unittest
from main import add_doc



class TestAddDoc(unittest.TestCase):
    def test_add_doc_correct(self):
        self.assertGreater(add_doc('1', '2', '3', '1'), 0)

    def test_add_doc_incorrect(self):
        self.assertLess(add_doc('1', '2', '3', '5'), 1)