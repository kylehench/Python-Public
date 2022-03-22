def minimumAbsoluteDifference(arr):
  arr.sort()
  return min(b-a for a, b in zip(arr[:-1], arr[1:]))