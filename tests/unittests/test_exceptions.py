import unittest
from nextmatter.exceptions import (
    NextMatterException,
    NextMatterCacheException,
    RatelimitBudgetExceeded,
    APIException,
    RecordNotFoundException,
    TooManyValuesException,
    InvalidQueryParamException,
    InvalidBodyParamException,
    InvalidPathParamException,
    InvalidPageSizeException
)

class TestExceptions(unittest.TestCase):

    def test_nextmatter_exception(self):
        with self.assertRaises(NextMatterException):
            raise NextMatterException("Test error")

    def test_nextmatter_cache_exception(self):
        with self.assertRaises(NextMatterCacheException):
            raise NextMatterCacheException("Test error")

    def test_ratelimit_budget_exceeded(self):
        with self.assertRaises(RatelimitBudgetExceeded):
            raise RatelimitBudgetExceeded("Test error")

    def test_api_exception(self):
        with self.assertRaises(APIException):
            raise APIException(response="Test response")

    def test_record_not_found_exception(self):
        with self.assertRaises(RecordNotFoundException):
            raise RecordNotFoundException("Test error")

    def test_too_many_values_exception(self):
        with self.assertRaises(TooManyValuesException):
            raise TooManyValuesException("Test error")

    def test_invalid_query_param_exception(self):
        with self.assertRaises(InvalidQueryParamException):
            raise InvalidQueryParamException("invalid_param", ["valid_param"])

    def test_invalid_body_param_exception(self):
        with self.assertRaises(InvalidBodyParamException):
            raise InvalidBodyParamException("invalid_param", ["valid_param"])

    def test_invalid_path_param_exception(self):
        with self.assertRaises(InvalidPathParamException):
            raise InvalidPathParamException("invalid_param", ["valid_param"])

    def test_invalid_page_size_exception(self):
        with self.assertRaises(InvalidPageSizeException):
            raise InvalidPageSizeException(600)

if __name__ == '__main__':
    unittest.main()