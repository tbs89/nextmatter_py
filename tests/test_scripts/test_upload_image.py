import unittest
from unittest.mock import patch
import sys
from nextmatter.scripts.upload_image import main

class TestUploadImageScript(unittest.TestCase):

    @patch('nextmatter.scripts.upload_image.NextMatterAPI')
    def test_main(self, MockAPI):
        mock_api_instance = MockAPI.return_value
        mock_api_instance.image.upload_image.return_value = {'status': 'success'}

        test_args = ['upload_image.py', 'tests/test_scripts/test_assets/test_image_random.png']
        with patch.object(sys, 'argv', test_args):
            main('tests/test_scripts/test_assets/test_image_random.png')
            mock_api_instance.image.upload_image.assert_called_once_with('tests/test_scripts/test_assets/test_image_random.png')

if __name__ == '__main__':
    unittest.main()