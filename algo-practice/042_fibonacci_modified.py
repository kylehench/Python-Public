import timeit
import math

def fibonacciModified1(t1, t2, n):
  arr = [t1, t2]
  for i in range(n-2):
    arr.append(arr[i]+arr[i+1]**2)
  return arr[-1]

def fibonacciModified2(t1, t2, n):
  t3 = t1 + t2**2
  for _ in range(n-2):
    t1, t2, t3 = t2, t3, t1 + t2**2
  return t3

n = 28
print(timeit.timeit(lambda: fibonacciModified1(0,1,n), number=1))
print(timeit.timeit(lambda: fibonacciModified2(0,1,n), number=1))