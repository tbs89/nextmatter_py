import unittest
from unittest.mock import MagicMock
from nextmatter.classes.form_field import FormField

class TestFormField(unittest.TestCase):

    def setUp(self):
        self.api = MagicMock()
        self.form_field = FormField(self.api, id='1', name='Test Field', type='text', required=True)

    def test_initialization(self):
        self.assertEqual(self.form_field.id, '1')
        self.assertEqual(self.form_field.name, 'Test Field')
        self.assertEqual(self.form_field.type, 'text')
        self.assertTrue(self.form_field.required)
        self.assertIsNone(self.form_field.options)

    def test_get_form_field_detail(self):
        self.api.session.get.return_value.json.return_value = {'id': '1', 'name': 'Test Field'}
        response = self.form_field.get_form_field_detail('workflow_id', 'step_id', 'form_field_id')
        self.assertEqual(response, {'id': '1', 'name': 'Test Field'})

if __name__ == '__main__':
    unittest.main()