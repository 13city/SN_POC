import unittest
from unittest.mock import patch, mock_open, MagicMock
import poc_data as pd

class TestPOCData(unittest.TestCase):

    def setUp(self):
        # Reset email_categories before each test
        pd.email_categories = {
            "interested": 10,
            "neutral": 10,
            "not interested": 10
        }
        self.greetings = ["Dear Team,", "Hello,", "Hi there,", "Greetings,"]

    def test_generate_email_content(self):
        """Test the generate_email_content function for each category."""
        for category in pd.email_categories.keys():
            content = pd.generate_email_content(category)
            self.assertIn("\n\n", content)
            self.assertTrue(any(content.startswith(greeting) for greeting in self.greetings))

    @patch('poc_data.input', create=True)
    def test_handle_existing_directory_keep(self, mocked_input):
        """Test handle_existing_directory to keep current emails."""
        mocked_input.return_value = '1'
        pd.handle_existing_directory()
        self.assertEqual(pd.email_categories['interested'], 10)

    @patch('poc_data.input', create=True)
    def test_handle_existing_directory_add(self, mocked_input):
        """Test handle_existing_directory to add more emails."""
        mocked_input.return_value = '2'
        with patch('os.listdir', return_value=['interested_1.txt', 'neutral_1.txt', 'not interested_1.txt']):
            pd.handle_existing_directory()
            self.assertEqual(pd.email_categories['interested'], 9)
            self.assertEqual(pd.email_categories['neutral'], 9)
            self.assertEqual(pd.email_categories['not interested'], 9)

    @patch('poc_data.input', create=True)
    def test_handle_existing_directory_replace(self, mocked_input):
        """Test handle_existing_directory to replace current emails."""
        mocked_input.return_value = '3'
        with patch('os.listdir', return_value=['interested_1.txt', 'neutral_1.txt', 'not interested_1.txt']), \
             patch('os.remove') as mock_remove:
            pd.handle_existing_directory()
            self.assertEqual(mock_remove.call_count, 3)
            self.assertEqual(pd.email_categories['interested'], 10)

    @patch('poc_data.handle_existing_directory')
    @patch('os.path.exists')
    @patch('os.makedirs')
    @patch('builtins.open', new_callable=mock_open)
    def test_create_test_emails(self, mock_file_open, mock_makedirs, mock_path_exists, mock_handle_existing):
        """Test create_test_emails for normal operations."""
        mock_path_exists.return_value = False
        pd.create_test_emails()
        mock_makedirs.assert_called_once_with(pd.test_directory)
        self.assertEqual(mock_file_open.call_count, 30)  # 10 per category

    @patch('builtins.print')
    @patch('builtins.open', new_callable=mock_open)
    def test_create_test_emails_error(self, mock_file_open, mock_print):
        """Test create_test_emails when file creation fails."""
        # Simulate the scenario for option 2
        pd.email_categories = {'interested': 9, 'neutral': 9, 'not interested': 9}
        total_files = sum(pd.email_categories.values())
        mock_file_open.side_effect = [None if i < total_files - 1 else IOError("File creation error") for i in range(total_files)]
        pd.create_test_emails()
        # Expect error on the last file to be created
        expected_error_file = f"test_emails/not interested_{pd.email_categories['not interested']}.txt"
        mock_print.assert_called_with(f"Error generating file {expected_error_file}: File creation error")

if __name__ == '__main__':
    unittest.main()
