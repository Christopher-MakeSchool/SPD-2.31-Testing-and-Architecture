# Test Exercise 2

import pytest
import math
from exercise_2 import get_age_carbon_14_dating

# TODO: Write a unit test which feed 0.35 to the function.
# The result should be '8680.34'.
# Does the function handles every possible input correctly?
# What if the input is zero or negative?
# Add the necessary logic to make sure the function handles every possible input properly.
# Then write a unit test againt this special case.

def test_get_age_carbon_14_dating():
    assert math.isclose(get_age_carbon_14_dating(0.35), 8680.34743)


# def test_all_age_carbon_14_dating():
#     for i in range(99):
#         assert math.isclose(get_age_carbon_14_dating(i/100))


def test_negative_age():
    with pytest.raises(TypeError):
        get_age_carbon_14_dating(-1)
    with pytest.raises(TypeError):
        get_age_carbon_14_dating(-50)
    with pytest.raises(IndexError):
        get_age_carbon_14_dating(-1.0)
    with pytest.raises(IndexError):
        get_age_carbon_14_dating(-0.35)


def test_non_float():
    with pytest.raises(TypeError):
        get_age_carbon_14_dating("hello")
    with pytest.raises(TypeError):
        get_age_carbon_14_dating("50")
    with pytest.raises(TypeError):
        get_age_carbon_14_dating(-10)
    with pytest.raises(TypeError):
        get_age_carbon_14_dating(10)
    with pytest.raises(TypeError):
        get_age_carbon_14_dating(True)
    with pytest.raises(TypeError):
        get_age_carbon_14_dating(False)
