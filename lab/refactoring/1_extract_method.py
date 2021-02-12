# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math 

def get_grades(n_student):
    grade_list = []
    # Get the inputs from the user
    for _ in range(0, n_student):
        grade_list.append(int(input('Enter a number: ')))
    return grade_list

def get_mean(grade_list):
    total = 0
    for grade in grade_list:
        total = total + grade
    return total / len(grade_list)

def get_sd(grade_list, mean=None):
    if mean is None:
        mean = get_mean(grade_list)
    sum_of_sqrs = 0
    for grade in grade_list:
        sum_of_sqrs += (grade - mean) ** 2
    return math.sqrt(sum_of_sqrs / len(grade_list))

def print_stat():
    # Calculate the mean and standard deviation of the grades
    grades = get_grades(5)
    mean = get_mean(grades)
    sd = get_sd(grades, mean=mean)
    
    # print out the mean and standard deviation in a nice format.
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(sd, 3))
    print('****** END ******')

print_stat()
