import unittest
from unittest.mock import patch
import sys
from nextmatter.scripts.upload_file import main

class TestUploadFileScript(unittest.TestCase):

    @patch('nextmatter.scripts.upload_file.NextMatterAPI')
    def test_main(self, MockAPI):
        mock_api_instance = MockAPI.return_value
        mock_api_instance.file.upload_file.return_value = {'status': 'success'}

        test_args = ['upload_file.py', 'tests/test_scripts/test_assets/test_file_random.pdf']
        with patch.object(sys, 'argv', test_args):
            main('tests/test_scripts/test_assets/test_file_random.pdf')
            mock_api_instance.file.upload_file.assert_called_once_with('tests/test_scripts/test_assets/test_file_random.pdf')

if __name__ == '__main__':
    unittest.main()