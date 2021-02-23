# Unit Testing With Pytest

## [Click Here to Get Started with Pytest](./pytest_instructions.md)

## Exercise 1

Assume you are a developer working for a company. They have asked you to write unit tests for one of their software packages. You encounter the following function:

```python
def get_average(li):
    sum = 0
    for num in li:
        sum += num
    mean = sum / len(li)
    return mean
```

Write a unit test for it. Does this function handle every possible input properly? If not, fix the bug and write a unit test against the bug.

## Solution to Exercise 1

We can write the following unit test to test get_average() function for normal inputs:

```python
def test_get_average_normal_use_case():
    assert math.isclose(get_average([1,2,3,4]), 2.5)
```

**Note:** Do not write,

```python
assert get_average([1,2,3,4]) == 2.5
```

Why? Because you should never ever compare floating point values directly using ‘==’. Floating-point error can causes the result of an calculation differ slightly from the correct answer. For example, consider the following multiplication:

```python
>>> 0.1*0.1*10
0.10000000000000002 
```

The result should be exactly 0.1 but it’s not. The ‘2’ at the end is a floating-point error. Now if in your program you had written

```python
0.1*0.1*10 == 0.1:
```

the condition would evaluate to ```False``` (!) as follows:

```python
>>> 0.1*0.1*10 == 0.1
False
```

Wow! Can you believe that? That’s why you should use math.isclose() function instead of ‘==’ to compare floating-point numbers:

```python
>>> math.isclose(0.1*0.1*10, 0.1)
True
```

What about integer numbers? Fortunately, you can safely compare integer numbers without any issue.
Now, going back to the second part of the question. Is there any input that can blow up the get_average() function? Yes, there is!

The function get_average() can throw the exception ‘ZeroDivisionError’, if it receives **an empty list:**

```python
mean = sum / len(li)
ZeroDivisionError: division by zero 
```

In order to handle this special case, we can check whether the input list is empty or not at the beginng of the function. If empty, we would return NaN:

```python
def get_average(li):
    if not li:
        return float('NaN')
    sum = 0
    for num in li:
    sum += num
    mean = sum / len(li)
    return mean
```

Now, let’s write a unit test for it:

```python
def test_get_average_empty_list():
    assert math.isnan(get_average([]))
```

## [Exercise 2](exercise_2.py): Carbon 14 Dating (to be submitted to gradescope)

Consider the following function that calculates the age of fossile: \
Read the TODO and implement the necessary changes and unit tests. \
Write a unit test for ```get_age_carbon_14_dating()``` function. \

```python
import math

T_HALF = 5730
DECAY_CONSTANT = -0.693

def get_age_carbon_14_dating(carbon_14_ratio):
"""Returns the estimated age of the sample in year.
carbon_14_ratio: the percent (0 < percent < 1) of carbon-14 
in the sample conpared to the amount in living 
tissue (unitless). 
"""
return math.log(carbon_14_ratio) / DECAY_CONSTANT * T_HALF 

# TODO: Write a unit test which feed 0.35 to the function. 
# The result should be '8680.34'. Does the function handles 
# every possible input correctly? What if the input is zero
# or negative?
# Add the necessary logic to make sure the function handle 
# every possible input properly. Then write a unit test againt 
# this special case.
```

## [Exercise 3](exercise_3.py): Calculate Grade Statistics (to be submitted to gradescope)

Write a unit test for ```calculate_stat()``` function.

```python
# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
# Refactored.
import math 

def display_grade_stat():
    """Gathers stats and print them out."""
    grade_list = read_input()
    # Calculate the mean and standard deviation of the grades
    mean, standard_deviation = calculate_stat(grade_list)
    # print out the mean and standard deviation in a nice format.
    print_stat(mean, standard_deviation)

def read_input():
    """Get the inputs from the user."""
    grade_list = []
    n_student = 5
    for _ in range(0, n_student):
        grade_list.append(int(input('Enter a number: ')))
    return grade_list

def calculate_stat(grade_list):
    """Calculate the mean and standard deviation of the grades."""
    total = 0
    for grade in grade_list:
        total = total + grade
    mean = total / len(grade_list)
    sum_of_sqrs = 0
    for grade in grade_list:
        sum_of_sqrs += (grade - mean) ** 2
    sd = math.sqrt(sum_of_sqrs / len(grade_list)) # standard deviation
    return mean, sd

def print_stat(mean, sd):
    """print out the mean and standard deviation in a nice format."""
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(sd, 3))
    print('****** END ******')

display_grade_stat()

```

## [Exercise 4](exercise_4.py): Extract Position (to be submitted to gradescope)

Write a unit test for ```extract_position()``` function.

```python
# by Kami Bigdely
# Replace nested conditional with gaurd clauses

def extract_position(line):
    if not line:
        pos = None
    else:
        if 'debug' in line or 'error' in line:
            pos = None
        else:
            if 'x:' in line:
                start_index = line.find('x:') + 2
                pos = line[start_index:] # from start_index to the end.
            else: 
                pos = None
    return pos

if __name__ == "__main__":
    result1 = extract_position('|error| numerical calculations could not converge.')
    print(result1)
    result2 = extract_position('|update| the positron location in the particle accelerator is x:21.432')
    print(result2)
```

## What and Where to Submit

Submit **exercises [2](exercise_2.py), [3](exercise_3.py) and [4](exercise_4.py)** to [Unit Testing 1](https://www.gradescope.com/courses/206382/assignments/1045905) on gradescope.

## Reference and further studies

1. [Pytest Installation and Getting Started](https://docs.pytest.org/en/stable/getting-started.html#getstarted)
2. [semaphoreci](https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest)
3. `Python Testing with pytest` book by Brian Okken.
