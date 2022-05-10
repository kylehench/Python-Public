import timeit

# Watson gives Sherlock an array of integers. His challenge is to find an element of the array such that the sum of all elements to the left is equal to the sum of all elements to the right.
# Example
#  is between two subarrays that sum to .
# The answer is  since left and right sum to .
# You will be given arrays of integers and must determine whether there is an element that meets the criterion. If there is, return YES. Otherwise, return NO.

def balancedSums1(arr):
  sum = 0
  arr_sum = []
  for x in arr:
    sum += x
    arr_sum.append(sum)
  if sum-arr[0]==0: return 'YES'
  for i in range(1,len(arr)):
    if arr_sum[i-1] == sum-arr_sum[i]: return 'YES'
  return 'NO'

def balancedSums2(arr):
  left = 0
  right = sum(arr)
  prev_x = 0
  for x in arr:
    left += prev_x
    right -= x
    if left==right: return 'YES'
    prev_x = x
  return 'NO'

arr = [1,2,3,4,5,6,5,4,3,2,1]
print(balancedSums2(arr))

print(timeit.timeit(lambda: balancedSums1(arr), number=1000))
print(timeit.timeit(lambda: balancedSums2(arr), number=1000))