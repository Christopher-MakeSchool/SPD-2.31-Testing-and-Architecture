# Test Exercise 3

import pytest
import math
from exercise_3 import calculate_stat

def test_calculate_stat():
    grade_list = [5, 3, 5, 1, 10, 6]
    mean = sum(grade_list)/len(grade_list)
    sum_of_sqrs = 0
    for grade in grade_list:
        sum_of_sqrs += (grade - mean) ** 2
    sd = math.sqrt(sum_of_sqrs / len(grade_list))  # standard deviation

    assert math.isclose(mean, 5.0)
    assert math.isclose(sd, 2.7688746209726918)
    assert math.isclose(calculate_stat(grade_list)[0], mean)
    assert math.isclose(calculate_stat(grade_list)[0], 5.0)
    assert math.isclose(calculate_stat(grade_list)[1], sd)
    assert math.isclose(calculate_stat(grade_list)[1], 2.768874620)
