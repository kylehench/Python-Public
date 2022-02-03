#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#
# Sam is a professor at the university and likes to round each student's  according to these rules:
# If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
# If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.

def gradingStudents(grades):
    new_grades = []
    for grade in grades:
        if grade < 38:
            new_grades.append(grade)
            continue
        next_multiple = 5*math.ceil(grade/5)
        if next_multiple - grade < 3:
            new_grades.append(next_multiple)
        else:
            new_grades.append(grade)
    return new_grades

if __name__ == '__main__':

    grades = [4, 73, 67, 38, 33]

    results = gradingStudents(grades)

    for result in results:
        print(result)