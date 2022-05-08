def fibonacciModified(t1, t2, n):
  arr = [t1, t2]
  for i in range(n-2):
    arr.append(arr[i]+arr[i+1]**2)
  return arr[-1]

print(fibonacciModified(0,1,6))