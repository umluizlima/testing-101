import unittest
import os
# Import my_app package
from my_app import create_app


# Define a new test case class
class MyTestCase(unittest.TestCase):

    # Define an application setup method
    def setUp(self):
        """
        Sets up the Flask application for testing
        """
        app = create_app('config.TestingConfig')
        self.app = app.test_client()

    def test_list_fruits_status_code_equals_200(self):
        """
        Test that '/fruits' response has status_code 200
        """
        result = self.app.get('/fruits')
        self.assertEqual(result.status_code, 200)

    def test_list_fruits_count(self):
        """
        Test that '/fruits' response has 4 elements
        """
        result = self.app.get('/fruits')
        self.assertEqual(len(result.json), 4)

    def test_list_fruits_has_banana(self):
        """
        Test that '/fruits' response has the expected content
        """
        result = self.app.get('/fruits')
        self.assertEqual(result.json[-1], {"type": "banana", "count": 7})


# Define a command-line entry point (unnecessary for python -m unittest)
if __name__ == "__main__":
    unittest.main()
