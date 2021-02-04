# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math

def print_stat(mean, sd):
    # print out the mean and standard deviation in a nice format.
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(sd, 3))
    print('****** END ******')


def get_grades():
    grade_list = []
    # Get the inputs from the user
    n_student = 5
    for _ in range(0, n_student):
        grade_list.append(int(input('Enter a number: ')))
    return grade_list


def calculate_grade_stats(grade_list):
    # Calculate the mean and standard deviation of the grades
    total = sum(grade_list)
    mean = total/len(grade_list)
    sum_of_sqrs = 0
    sd = 0  # standard deviation

    for grade in grade_list:
      sum_of_sqrs += (grade - mean) ** 2

    sd = math.sqrt(sum_of_sqrs / len(grade_list))
    return mean, sd


if __name__ == "__main__":
    grade_list = get_grades()
    mean, sd = calculate_grade_stats(grade_list)
    print_stat(mean, sd)
