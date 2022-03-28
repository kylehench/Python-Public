def missingNumbers(arr, brr):
  data = {}
  for i in arr:
    if i in data:
      data[i] += 1
    else:
      data[i] = 1
  missing = {}
  brr.sort()
  for i in brr:
    if i in data and data[i] >=1:
      data[i] -= 1
    else:
      missing[i] = 1
  return missing.keys()
      


test_case = ([203,204,205,206,207,208,203,204,205,206],[203,204,204,205,206,207,205,208,203,206,205,206,204])

print(missingNumbers(*test_case))