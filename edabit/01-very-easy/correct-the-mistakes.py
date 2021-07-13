"""
Correct the Mistakes
Fix the code in the code tab to pass this challenge (only syntax errors). Look at the examples below to get an idea of what the function should do.

Examples
squared(5) ➞ 25

squared(9) ➞ 81

squared(100) ➞ 10000
Notes
READ EVERY WORD CAREFULLY, CHARACTER BY CHARACTER!
Don't overthink this challenge; it's not supposed to be hard.
"""
from edabit.Test import Test


def squared(b):
    return b * b


if __name__ == '__main__':
    Test.assert_equals(squared(10), 100)
    Test.assert_equals(squared(69), 4761)
    Test.assert_equals(squared(666), 443556)
    Test.assert_equals(squared(-21), 441)
    Test.assert_equals(squared(21), 441)
