def getTotalX(a, b):
  test_max = max(b)
  integers = []
  for i in range(1,test_max+1):
    if sum(el%i for el in b) == 0 and sum(i%el for el in a) == 0:
      integers.append(i)
  return len(integers)

print(getTotalX([2,6],[24,36]))