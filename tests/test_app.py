# tests/test_app.py

import unittest
from unittest.mock import patch
from app import app

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('app.articles_collection.find')
    def test_index_page(self, mock_find):
        """Test if the index page loads correctly."""
        mock_find.return_value = []
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    @patch('app.articles_collection.insert_one')
    def test_new_article_page(self, mock_insert_one):
        """Test if the new article page loads correctly."""
        response = self.app.post('/new', data=dict(title="Test Title", content="Test Content", author="Test Author"))
        self.assertEqual(response.status_code, 302)  # Should redirect after posting

    @patch('app.articles_collection.find_one')
    def test_view_article_page(self, mock_find_one):
        """Test if the view article page loads correctly."""
        mock_find_one.return_value = {"_id": "someid", "title": "Test Title", "content": "Test Content", "author": "Test Author"}
        response = self.app.get('/article/someid')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
