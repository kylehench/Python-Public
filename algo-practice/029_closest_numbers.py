from timeit import timeit

def closestNumbers(arr):
  arr.sort()
  results = {}
  
  for i in range(len(arr)- 1):
    diff = abs(arr[i] - arr[i+1])
    
    if diff in results:
      results[diff] += [arr[i], arr[i+1]]
    else:
      results[diff] = [arr[i], arr[i+1]]
  
  min_abs = min(results.keys())
  return results[min_abs]
  
def closestNumbers1(arr):
  arr.sort()
  diff_min = min(b-a for a, b in zip(arr[:len(arr)-1], arr[1:]))
  out = []
  for a, b in zip(arr[:len(arr)-1], arr[1:]):
    if b-a == diff_min:
      out += [a,b]
  return out

test = [5,2,3,4,1]
print(closestNumbers(test))

print(timeit(lambda: closestNumbers1(test), number=10000))