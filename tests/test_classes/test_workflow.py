import unittest
from unittest.mock import MagicMock
from nextmatter.classes.workflow import Workflow

class TestWorkflow(unittest.TestCase):

    def setUp(self):
        self.api = MagicMock()
        self.workflow = Workflow(self.api, id='1', name='Test Workflow', created_at='2023-01-01T00:00:00Z', updated_at='2023-01-01T00:00:00Z')

    def test_initialization(self):
        self.assertEqual(self.workflow.id, '1')
        self.assertEqual(self.workflow.name, 'Test Workflow')
        self.assertEqual(self.workflow.created_at, '2023-01-01T00:00:00Z')
        self.assertEqual(self.workflow.updated_at, '2023-01-01T00:00:00Z')

    def test_list_workflows(self):
        self.api.session.get.return_value.json.return_value = [{'id': '1', 'name': 'Test Workflow'}]
        response = self.workflow.list_workflows()
        self.assertEqual(response, [{'id': '1', 'name': 'Test Workflow'}])

    def test_get_workflow(self):
        self.api.session.get.return_value.json.return_value = {'id': '1', 'name': 'Test Workflow'}
        response = self.workflow.get_workflow('1')
        self.assertEqual(response, {'id': '1', 'name': 'Test Workflow'})

if __name__ == '__main__':
    unittest.main()