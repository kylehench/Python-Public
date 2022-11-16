# Given an array of equal-length strings, you'd like to know if it's possible to rearrange the order of the elements in such a way that each consecutive pair of strings differ by exactly one character. Return true if it's possible, and false if not.

# Note: You're only rearranging the order of the strings, not the order of the letters within the strings!

def solution(inputArray):
  def one_diff(a, b):
    # returns True if there is exactly 1 difference between two equal-length strings
    return sum(i!=j for i, j in zip(a, b)) == 1
  
  def arrange(arr, pool):
    if not pool:
      # successful case if pool has been depleted
      return True
    for item in pool:
      # see whether each item in pool can succeed the last item in arr. If so, make a copy of arr and pool, and recursively call arrange on modified copies.
      if one_diff(arr[-1], item):
        arr_new = arr.copy() + [item]
        pool_new = pool.copy()
        pool_new.remove(item)
        if arrange(arr_new, pool_new):
          return True     
    return False

   
  return any(arrange([inputArray[i]], inputArray[0:i]+inputArray[i+1:]) for i in range(len(inputArray)))