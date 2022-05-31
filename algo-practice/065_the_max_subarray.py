def maxSubarray(arr):
  max_sums = [arr[0]]
  sum_non_contiguous = max(0, arr[0])
  for i in range(1,len(arr)):
    max_sums.append(max(max_sums[i-1]+arr[i], arr[i]))
    if arr[i]>0:
      sum_non_contiguous += arr[i]
  if sum_non_contiguous==0:
    sum_non_contiguous = max(arr)
  return [max(max_sums), sum_non_contiguous]

test_cases = (
  [-1,2,3,-4,5,10],
  [1,2,3,4,],
  [2,-1,2,3,4,-5],
)

for case in test_cases:
  print(maxSubarray(case))