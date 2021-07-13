"""
Power Calculator
Create a function that takes voltage and current and returns the calculated power.

Examples
circuit_power(230, 10) ➞ 2300

circuit_power(110, 3) ➞ 330

circuit_power(480, 20) ➞ 9600
Notes
Requires basic calculation of electrical circuits (see Resources for info).
"""
from edabit.Test import Test
def circuit_power(a, b):
    return a*b

if __name__ == '__main__':
    Test.assert_equals(circuit_power(110, 3), 330)
    Test.assert_equals(circuit_power(230, 10), 2300)
    Test.assert_equals(circuit_power(480, 20), 9600)