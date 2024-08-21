import unittest
from unittest.mock import MagicMock
from nextmatter.classes.file import File

class TestFile(unittest.TestCase):

    def setUp(self):
        self.api = MagicMock()
        self.file = File(self.api, created_time='2023-01-01T00:00:00Z')

    def test_initialization(self):
        self.assertEqual(self.file.created_time, '2023-01-01T00:00:00Z')
        self.assertIsNone(self.file.process)
        self.assertIsNone(self.file.process_instance)
        self.assertIsNone(self.file.file_uri)

    def test_upload_file(self):
        self.api.session.post.return_value.json.return_value = {'status': 'success'}
        response = self.file.upload_file('test_file.txt')
        self.assertEqual(response, {'status': 'success'})

if __name__ == '__main__':
    unittest.main()