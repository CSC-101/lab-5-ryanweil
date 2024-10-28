import data

# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.
from typing import Any

class Time:
    def __init__(self, hour: int, minute: int, second: int):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __eq__(self, other: Any) -> bool:
        # Check if other is an instance of Time and compare attributes
        if isinstance(other, Time):
            return (self.hour == other.hour and
                    self.minute == other.minute and
                    self.second == other.second)
        return False


# Part 2
   # The function for Part 2 should be within the class in data.py.
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


# Part 3
from data import Time  # Import the Time class from data.py

def time_add(time1: Time, time2: Time) -> Time:
    # Add seconds and handle overflow into minutes
    new_second = time1.second + time2.second
    extra_minute = new_second // 60
    new_second = new_second % 60

    # Add minutes, including any extra from seconds, and handle overflow into hours
    new_minute = time1.minute + time2.minute + extra_minute
    extra_hour = new_minute // 60
    new_minute = new_minute % 60

    # Add hours, including any extra from minutes
    new_hour = time1.hour + time2.hour + extra_hour

    # Return a new Time object with the calculated hour, minute, and second
    return Time(new_hour, new_minute, new_second)


# Part 4
def is_descending(lst: list[float]) -> bool:
    return all(lst[i] > lst[i + 1] for i in range(len(lst) - 1))


# Part 5
from typing import List, Optional

def largest_between(numbers: List[int], lower: int, upper: int) -> Optional[int]:
    # Handle cases where the range is invalid (lower > upper)
    if lower > upper:
        return None

    # Adjust lower and upper bounds if they are out of bounds
    lower = max(0, lower)
    upper = min(len(numbers) - 1, upper)

    # If the adjusted bounds create an empty range, return None
    if lower > upper:
        return None

    # Find the index of the maximum value within the range
    max_index = lower
    for i in range(lower, upper + 1):
        if numbers[i] > numbers[max_index]:
            max_index = i

    return max_index


# Part 6
from typing import List, Optional
from math import pow  # Optional, can also use ** operator

# Assuming Point is defined as follows (adapt if it differs in your files):
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

def furthest_from_origin(points: List[Point]) -> Optional[int]:
    # Return None if the list is empty
    if not points:
        return None

    # Find the index of the point with the largest distance from origin
    max_index = 0
    max_distance_squared = points[0].x ** 2 + points[0].y ** 2  # Initial distance squared

    for i in range(1, len(points)):
        distance_squared = points[i].x ** 2 + points[i].y ** 2
        if distance_squared > max_distance_squared:
            max_distance_squared = distance_squared
            max_index = i

    return max_index
