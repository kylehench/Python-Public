# A left rotation operation on an array of size n shifts each of the array's elements 1 unit to the left. Given an integer, d, rotate the array that many steps left and return the result.
from timeit import timeit

def rotateLeft(d, arr):
  left = arr[d:]
  right = arr[:d]
  return left+right

def rotateLeft1(d, arr):
  period = len(arr)
  return [arr[(i+d)%period] for i in range(period)]

test = (2, [1,2,3,4,5]) # expect [3, 4, 5, 1, 2]
print(rotateLeft(*test))

repetitions = 100000
print(timeit(lambda: rotateLeft(*test), number=repetitions))
print(timeit(lambda: rotateLeft1(*test), number=repetitions))