import unittest
# Import sum() from the my_sum package
from my_sum import sum
from fractions import Fraction


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

    # Every test follows 3 basic steps
    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        # Create your inputs
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        # Execute the code, capturing the output
        result = sum(data)
        # Compare the output with an expected result
        self.assertEqual(result, 1)

    # It is possible to handle expected failures in tests
    def test_bad_type(self):
        """
        Test that it throws a TypeError when given bad input
        """
        # Create an input that should raise an error when used
        data = "banana"
        # .assertRaises() is used as a context-manager
        with self.assertRaises(TypeError):
            # The output is captured within the with block
            result = sum(data)


# Define a command-line entry point
if __name__ == "__main__":
    unittest.main()
