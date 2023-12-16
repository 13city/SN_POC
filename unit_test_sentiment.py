import unittest
from unittest.mock import patch, mock_open, MagicMock
import sentiment as sa
import io
import sys

class TestSentimentAnalysis(unittest.TestCase):

    def setUp(self):
        """Redirect stdout to suppress print statements during testing."""
        self.held, sys.stdout = sys.stdout, io.StringIO()

    def tearDown(self):
        """Reset stdout after each test."""
        sys.stdout = self.held

    def test_normalize_text(self):
        """Test the normalize_text function for various scenarios."""
        test_texts = {
            "Check out this link: http://example.com\nContact: test@example.com": "Check out this link Contact",
            "Hi there,\n\nThanks!\n\nBest regards,\nJohn Doe": "Hi there",
            "Special characters & symbols should be removed!": "Special characters symbols should be removed"
        }
        for text, expected in test_texts.items():
            self.assertEqual(sa.normalize_text(text), expected)

    def test_heuristic_check_various_cases(self):
        """Test the heuristic_check function for various cases."""
        test_cases = {
            "This sounds great! I'd love to learn more.": "interested",
            "No thanks, not interested in this offer.": "not interested",
            "I will review your proposal and get back to you.": None,
            "": None,  # Edge case: Empty string
            "This email is ambiguous and unclear.": None  # Edge case: Ambiguous content
        }
        for text, expected in test_cases.items():
            self.assertEqual(sa.heuristic_check(text), expected)

    @patch('sentiment.load_model')
    @patch('glob.glob')
    def test_process_emails_normal_case(self, mock_glob, mock_load_model):
        """Test the process_emails function for normal case."""
        mock_glob.return_value = ['/path/to/test_email.txt']
        mock_load_model.return_value = MagicMock(return_value=[{"label": "NEGATIVE", "score": 0.1}])

        with patch('builtins.open', new_callable=mock_open, read_data="This is a test email content."):
            sa.process_emails("dummy_directory", mock_load_model())
            mock_load_model.assert_called()

    @patch('sentiment.load_model')
    @patch('glob.glob')
    def test_process_emails_file_reading_error(self, mock_glob, mock_load_model):
        """Test the process_emails function when file reading fails."""
        mock_glob.return_value = ['/path/to/test_email.txt']
        mock_load_model.return_value = MagicMock(return_value=[{"label": "NEGATIVE", "score": 0.1}])

        with patch('builtins.open', mock_open()) as mock_file:
            mock_file.side_effect = OSError("File not found")
            with self.assertRaises(OSError):
                sa.process_emails("dummy_directory", mock_load_model())

    @patch('transformers.pipeline')
    @patch('glob.glob')
    def test_process_emails_model_error(self, mock_glob, mock_pipeline):
        """Test the process_emails function when model analysis fails."""
        mock_glob.return_value = ['/path/to/test_email.txt']
        mock_pipeline.side_effect = Exception("Model error")

        with patch('builtins.open', new_callable=mock_open, read_data="Email content"):
            with self.assertRaises(Exception):
                sa.process_emails("dummy_directory", mock_pipeline())

if __name__ == '__main__':
    unittest.main()
