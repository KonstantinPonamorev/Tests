import unittest
from main import doc_list



class TestDocList(unittest.TestCase):
    def test_doc_list(self):
        self.assertIsNotNone(doc_list())