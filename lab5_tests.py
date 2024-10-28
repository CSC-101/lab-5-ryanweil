import data
import lab5
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3
    import unittest
    from data import Time
    from lab5 import time_add  # Import time_add from lab5.py

    class TestTimeAdd(unittest.TestCase):
        def test_time_add_no_carryover(self):
            time1 = Time(1, 20, 30)
            time2 = Time(2, 10, 15)
            result = time_add(time1, time2)
            expected = Time(3, 30, 45)
            self.assertEqual(result, expected)

        def test_time_add_with_carryover(self):
            time1 = Time(1, 59, 45)
            time2 = Time(0, 1, 30)
            result = time_add(time1, time2)
            expected = Time(2, 1, 15)  # 45 + 30 seconds carries over to 1 extra minute
            self.assertEqual(result, expected)

    if __name__ == '__main__':
        unittest.main()

    # Part 4
    import unittest
    from lab5 import is_descending  # Import is_descending from lab5.py, adjust if the file name differs

    # Define a test case class for the lab functions
    class TestCases(unittest.TestCase):
        def test_is_descending(self):
            # Test case 1: List is strictly descending
            self.assertTrue(is_descending([5.0, 4.0, 3.0, 2.0, 1.0]), "Test case 1 failed")

            # Test case 2: List is not strictly descending
            self.assertFalse(is_descending([5.0, 5.0, 3.0, 2.0]), "Test case 2 failed")

            # Test case 3: Empty list (edge case)
            self.assertTrue(is_descending([]), "Test case 3 failed")

            # Test case 4: List with one element (edge case)
            self.assertTrue(is_descending([1.0]), "Test case 4 failed")

    # This allows you to run the tests directly from the command line or within an IDE like PyCharm
    if __name__ == '__main__':
        unittest.main()

    # Part 5
    import unittest
    from lab5 import largest_between  # Adjust the import path as needed

    class TestCases(unittest.TestCase):
        def test_largest_between(self):
            # Test case 1: Standard case with a clear maximum within range
            self.assertEqual(largest_between([1, 3, 5, 7, 9], 1, 3), 3, "Test case 1 failed")

            # Test case 2: Lower bound is greater than upper bound (should return None)
            self.assertIsNone(largest_between([1, 3, 5, 7, 9], 3, 1), "Test case 2 failed")

            # Test case 3: Bounds are partially out of range, adjusting to valid range
            self.assertEqual(largest_between([1, 2, 3, 4, 5], -1, 3), 3, "Test case 3 failed")

            # Test case 4: Upper bound out of range, adjusted to valid range
            self.assertEqual(largest_between([1, 2, 10, 3, 4], 2, 10), 2, "Test case 4 failed")

            # Test case 5: Lower and upper are the same, should return that index

    # Part 6


import unittest
from lab5 import Point, furthest_from_origin  # Adjust imports as needed


class TestCases(unittest.TestCase):
    def test_furthest_from_origin(self):
        # Test case 1: Points with varying distances from the origin
        points = [Point(1, 2), Point(3, 4), Point(6, 8), Point(1, 1)]
        self.assertEqual(furthest_from_origin(points), 2, "Test case 1 failed")

        # Test case 2: Empty list of points (should return None)
        points = []
        self.assertIsNone(furthest_from_origin(points), "Test case 2 failed")

        # Test case 3: Points with the same distance from origin
        points = [Point(1, 1), Point(-1, -1), Point(1, 1)]
        self.assertEqual(furthest_from_origin(points), 0, "Test case 3 failed")


if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()
