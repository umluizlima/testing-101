def test_sum_passes():
    """Assert if the sum of 1, 2 and 3 equals 6.

    As the asserted result is correct, this will pass.
    """
    assert sum([1, 2, 3]) == 6, "Should be 6"


def test_sum_fails():
    """Assert if the sum of 1, 1 and 1 equals 6.

    As the asserted result is incorrect, this will fail with an AssertionError
    and the message "Should be 6".
    """
    assert sum([1, 1, 1]) == 6, "Should be 6"


if __name__ == "__main__":
    test_sum_passes()
    # test_sum_fails()
    print("Everything passed")
