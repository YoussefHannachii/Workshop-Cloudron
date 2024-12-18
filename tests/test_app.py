import unittest
from app import app  # Assuming your Flask app is in app.py

class FlaskAppTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Setup the test client before all tests."""
        cls.client = app.test_client()
        cls.client.testing = True
    
    def test_index_page(self):
        """Test if the index page loads correctly and contains articles."""
        # Simulate GET request to the index page
        response = self.client.get('/')
        
        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Check if the page contains the word "Articles" (as per your template)
        self.assertIn(b'Articles', response.data)
        
        # Optionally, check if a specific article is in the response (if there are any articles)
        # Make sure to have a sample article in your database or mock it
        self.assertIn(b'Add New Article', response.data)
    
    # You can add other unit tests as needed (e.g., for article creation, editing, deletion)

if __name__ == '__main__':
    unittest.main()
