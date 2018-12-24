"""Convert the previous example to a unittest test case."""

# Import unittest from the standard library
import unittest


# Create a class called TestSum that inherits from the TestCase class
class TestSum(unittest.TestCase):

    # Convert the test functions into methods by adding self as argument
    def test_sum_list(self):
        # Change assertions to use self.assertEqual() on the TestCase class
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")


if __name__ == "__main__":
    # Change the command-line entry point to call unittest.main()
    unittest.main()
