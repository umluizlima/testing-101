import unittest
# Import my_app package
from my_app import create_app


# Define a new test case class
class MyTestCase(unittest.TestCase):

    # Define an application setup method
    def setUp(self):
        """
        Sets up the Flask application for testing
        """
        app = create_app()
        app.testing = True
        self.app = app.test_client()

    def test_home_status_code_equals_200(self):
        """
        Test that '/' response has status_code 200
        """
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_home_content(self):
        """
        Test that '/' response has the expected content
        """
        result = self.app.get('/')
        self.assertEqual(result.data, b"Howdy from home!")


# Define a command-line entry point (unnecessary for python -m unittest)
if __name__ == "__main__":
    unittest.main()
