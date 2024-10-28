import data
import unittest


class TestCases(unittest.TestCase):
    #### Time tests
    def test_Time_1(self):
        time = data.Time(7, 20, 1)
        self.assertEqual(7, time.hour)
        self.assertEqual(20, time.minute)
        self.assertEqual(1, time.second)


    def test_Time_2(self):
        time = data.Time(4, 19, 45)
        self.assertEqual(4, time.hour)
        self.assertEqual(19, time.minute)
        self.assertEqual(45, time.second)


    #### Add tests for Time.__eq__
    import unittest
    from lab5 import Time  # Ensure this imports `Time` from the correct file

    class TestTime(unittest.TestCase):
        def test_equal_times(self):
            time1 = Time(10, 30, 25)
            time2 = Time(10, 30, 25)
            self.assertEqual(time1, time2)  # Should be True

        def test_different_hour(self):
            time1 = Time(10, 30, 25)
            time2 = Time(11, 30, 25)
            self.assertNotEqual(time1, time2)  # Should be False

        def test_different_minute(self):
            time1 = Time(10, 30, 25)
            time2 = Time(10, 31, 25)
            self.assertNotEqual(time1, time2)  # Should be False

        def test_different_second(self):
            time1 = Time(10, 30, 25)
            time2 = Time(10, 30, 26)
            self.assertNotEqual(time1, time2)  # Should be False

        def test_non_time_comparison(self):
            time1 = Time(10, 30, 25)
            not_a_time = "10:30:25"
            self.assertNotEqual(time1, not_a_time)  # Should be False

    if __name__ == '__main__':
        unittest.main()

    #### Add tests for Time.__repr__
    import unittest
    from data import Time

    class TestTime(unittest.TestCase):
        # Existing tests here

        def test_repr_format(self):
            time = Time(10, 30, 25)
            expected_repr = "Time(hour=10, minute=30, second=25)"
            self.assertEqual(repr(time), expected_repr)

        def test_repr_format_different_time(self):
            time = Time(5, 45, 59)
            expected_repr = "Time(hour=5, minute=45, second=59)"
            self.assertEqual(repr(time), expected_repr)

    if __name__ == '__main__':
        unittest.main()

    #### Point tests
    def test_Point_1(self):
        point = data.Point(7, 20)
        self.assertAlmostEqual(7, point.x)
        self.assertAlmostEqual(20, point.y)


    def test_Point_2(self):
        point = data.Point(4, 19)
        self.assertAlmostEqual(4, point.x)
        self.assertAlmostEqual(19, point.y)


    def test_Point_eq_1(self):
        point1 = data.Point(1, 20)
        point2 = data.Point(1, 20)
        self.assertEqual(point1, point2)


    def test_Point_eq_2(self):
        point1 = data.Point(1, 20)
        self.assertEqual(point1, point1)


    def test_Point_eq_3(self):
        point1 = data.Point(1, 20)
        point2 = data.Point(2, 20)
        self.assertNotEqual(point1, point2)


    def test_Point_eq_4(self):
        point = data.Point(1, 20)
        other = 1.20
        self.assertNotEqual(point, other)


    def test_Point_repr(self):
        point = data.Point(5, 75)
        self.assertEqual('Point(5, 75)', repr(point))


if __name__ == '__main__':
    unittest.main()
