import unittest
from nextmatter.api import NextMatterAPI
from nextmatter.exceptions import NextMatterException

class TestNextMatterAPI(unittest.TestCase):

    def setUp(self):
        self.api_key = 'test_api_key'
        self.api = NextMatterAPI(api_key=self.api_key)

    def test_initialization(self):
        self.assertEqual(self.api.api_key, self.api_key)
        self.assertIsNotNone(self.api.file)
        self.assertIsNotNone(self.api.image)
        self.assertIsNotNone(self.api.instance)
        self.assertIsNotNone(self.api.workflow)
        self.assertIsNotNone(self.api.form_field)

    def test_initialization_without_api_key(self):
        with self.assertRaises(ValueError):
            NextMatterAPI(api_key=None)

    def test_initialization_exception(self):
        with self.assertRaises(NextMatterException):
            NextMatterAPI(api_key='')

if __name__ == '__main__':
    unittest.main()