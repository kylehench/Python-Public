def quicksort(arr):
  def partition(i0, j0):
    i, j = i0, j0
    mid_idx = (i + j)//2
    mid_val = arr[mid_idx]
    while i != j:
      while arr[i] < mid_val and i !=j:
        i += 1
      while arr[j] >= mid_val and i !=j:
        j -= 1
      arr[i], arr[j] = arr[j], arr[i]
    if j0-i0 > 1:
      partition(i0, mid_idx)
      partition(mid_idx, j0)

  partition(0, len(arr)-1)
  return arr

print(quicksort([1, 3, 6, 8, 9, 10, 12, 13, 16, 18, 20, 21, 22, 23, 24, 25, 27, 30, 32, 33, 34, 39, 40, 41, 42, 43, 44, 46, 48, 50, 53, 56, 57, 59, 60, 61, 63, 65, 67, 68, 69, 70, 73, 74, 75, 76, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 89, 90, 91, 92, 94, 95, 96, 98, 99]))