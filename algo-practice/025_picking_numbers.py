# Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to 1.
# Function Description
# Complete the pickingNumbers function in the editor below.
# pickingNumbers has the following parameter(s):
# int a[n]: an array of integers
# Returns
# int: the length of the longest subarray that meets the criterion

from timeit import timeit as ti

def pickingNumbers(a):
  a.sort()
  i_max = len(a)-1
  max_length = 1 # length of the longest subarray
  for i1 in range(i_max+1):
    if i1 > 0 and a[i1] == a[i1-1]: # skip testing of repeated values
      continue
    i2 = i1
    while i2<i_max and a[i2+1]-a[i1]<=1: # test next i2
      i2 += 1 # iterate if absolute diff <= 1
    length = i2-i1+1
    if length > max_length:
      max_length = length
  return max_length

# unoptimized version
def pickingNumbers1(a):
  a.sort()
  i_max = len(a)-1
  max_length = 1 # length of the longest subarray
  for i1 in range(i_max+1):
    i2 = i1
    while i2<i_max and a[i2+1]-a[i1]<=1: # test next i2
      i2 += 1 # iterate if absolute diff <= 1
    length = i2-i1+1
    if length > max_length:
      max_length = length
  return max_length

test_case = "4 97 5 97 97 4 97 4 97 97 97 97 4 4 5 5 97 5 97 99 4 97 5 97 97 97 5 5 97 4 5 97 97 5 97 4 97 5 4 4 97 5 5 5 4 97 97 4 97 5 4 4 97 97 97 5 5 97 4 97 97 5 4 97 97 4 97 97 97 5 4 4 97 4 4 97 5 97 97 97 97 4 97 5 97 5 4 97 4 5 97 97 5 97 5 97 5 97 97 97"
test_case = [int(num) for num in test_case.split(" ")]
print(pickingNumbers(test_case)) # correct answer is 50

repetitions = 1000
print(f'Optimized: {ti(lambda: pickingNumbers(test_case), number = repetitions)}')
print(f'Not optimized: {ti(lambda: pickingNumbers1(test_case), number = repetitions)}')