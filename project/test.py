import unittest

# Import sum() from the my_sum package
from my_sum import sum


# Define a new test case class
class TestSum(unittest.TestCase):

    # Define a test method to test a list of integers
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)


# Define a command-line entry point
if __name__ == "__main__":
    unittest.main()
