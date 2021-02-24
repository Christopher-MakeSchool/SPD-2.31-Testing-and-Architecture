# Test Exercise 4

import pytest
import math
from exercise_4 import extract_position

def test_extract_position():
    assert extract_position(
        '|error| numerical calculations could not converge.') == None
    assert extract_position(
        '|debug| numerical calculations could not converge.') == None
    assert extract_position(
        '|update| the positron location in the particle accelerator is x:21.432') == "21.432"
    assert extract_position(
        '|update| the positron location in the particle accelerator is x:43.283') == "43.283"
    assert extract_position(
        '|update| the positron location in the particle accelerator is x:175.319') == "175.319"
