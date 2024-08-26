import unittest
from nextmatter.endpoint_validator import EndpointValidator
from nextmatter.exceptions import InvalidQueryParamException, InvalidParamFormatException

class TestEndpointValidator(unittest.TestCase):

    def setUp(self):
        self.validator = EndpointValidator('create_instance')

    def test_validate_params_invalid_param(self):
        with self.assertRaises(InvalidQueryParamException):
            self.validator.validate_params({'invalid_param': 'value'}, 'body_params')

    def test_validate_params_invalid_format(self):
        with self.assertRaises(InvalidParamFormatException):
            self.validator.validate_params({'name': 123}, 'body_params')

    def test_build_url(self):
        url = self.validator.build_url({'id': '1'})
        self.assertEqual(url, 'https://core.nextmatter.com/api/instances/1/')

    def test_make_request(self):
        request_data = self.validator.make_request(body_params={'name': 'Test Instance'})
        self.assertEqual(request_data['method'], 'post')
        self.assertEqual(request_data['url'], 'https://core.nextmatter.com/api/instances/')
        self.assertEqual(request_data['body_params'], {'name': 'Test Instance'})

if __name__ == '__main__':
    unittest.main()