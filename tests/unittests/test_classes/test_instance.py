import unittest
from unittest.mock import MagicMock
from nextmatter.classes.instance import Instance
from nextmatter.exceptions import InvalidPageSizeException

class TestInstance(unittest.TestCase):

    def setUp(self):
        self.api = MagicMock()
        self.instance = Instance(self.api, id='1', name='Test Instance', process='Test Process')

    def test_initialization(self):
        self.assertEqual(self.instance.id, '1')
        self.assertEqual(self.instance.name, 'Test Instance')
        self.assertEqual(self.instance.process, 'Test Process')
        self.assertIsNone(self.instance.deadline)
        self.assertIsNone(self.instance.priority)

    def test_create_instance(self):
        self.api.session.post.return_value.json.return_value = {'id': '1', 'name': 'Test Instance'}
        response = self.instance.create_instance({'name': 'Test Instance'})
        self.assertEqual(response, {'id': '1', 'name': 'Test Instance'})

    def test_delete_instances(self):
        self.api.session.delete.return_value.json.return_value = {'status': 'success'}
        response = self.instance.delete_instances(['1'])
        self.assertEqual(response, {'status': 'success'})

    def test_list_instances_invalid_page_size(self):
        with self.assertRaises(InvalidPageSizeException):
            self.instance.list_instances(page_size=600)

if __name__ == '__main__':
    unittest.main()