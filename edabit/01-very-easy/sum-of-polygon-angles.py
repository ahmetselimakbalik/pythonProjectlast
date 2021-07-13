"""
Sum of Polygon Angles
Given an n-sided regular polygon n, return the total sum of internal angles (in degrees).

Examples
sum_polygon(3) ➞ 180

sum_polygon(4) ➞ 360

sum_polygon(6) ➞ 720
Notes
n will always be greater than 2.
The formula (n - 2) x 180 gives the sum of all the measures of the angles of an n-sided polygon.
"""
from edabit.Test import Test


def sum_polygon(n):
    return (n - 2) * 180


if __name__ == '__main__':
    from time import perf_counter

    tic = perf_counter()
    Test.assert_equals(sum_polygon(3), 180)
    Test.assert_equals(sum_polygon(4), 360)
    Test.assert_equals(sum_polygon(5), 540)
    Test.assert_equals(sum_polygon(6), 720)
    Test.assert_equals(sum_polygon(7), 900)
    Test.assert_equals(sum_polygon(8), 1080)
    Test.assert_equals(sum_polygon(9), 1260)
    Test.assert_equals(sum_polygon(10), 1440)
    Test.assert_equals(sum_polygon(11), 1620)
    Test.assert_equals(sum_polygon(12), 1800)
