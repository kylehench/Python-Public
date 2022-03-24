# You will be given a list of integers, arr, and a single integer k. You must create an array of length k from elements of arr such that its unfairness is minimized. Call that array arr'. Unfairness of an array is calculated as max(arr') - min(arr')

# Where:
# - max denotes the largest integer in arr'
# - min denotes the smallest integer in arr'

def maxMin(k, arr):
  arr.sort()
  arr_len = len(arr)
  return min([b-a for a, b in zip(arr[:arr_len-k+1], arr[k-1:arr_len])])

test_case = [1,4,7,2]
print(maxMin(2,test_case))