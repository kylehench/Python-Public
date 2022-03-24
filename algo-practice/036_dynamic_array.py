# Declare a 2-dimensional array, arr, of n empty arrays. All arrays are zero indexed.
# Declare an integer, lastAnswer, and initialize it to 0.
# There are 2 types of queries, given as an array of strings for you to parse:
# Query: 1 x y
# Let .
# Append the integer  to .
# Query: 2 x y
# Let .
# Assign the value  to .
# Store the new value of  to an answers array.
# Note:  is the bitwise XOR operation, which corresponds to the ^ operator in most languages. Learn more about it on Wikipedia.  is the modulo operator.
# Finally, size(arr[idx]) is the number of elements in arr[idx]
# Function Description
# Complete the dynamicArray function below.
# dynamicArray has the following parameters:
# - int n: the number of empty arrays to initialize in 
# - string queries[q]: query strings that contain 3 space-separated integers
# Returns
# int[]: the results of each type 2 query in the order they are presented

def dynamicArray(n, queries):
  arr = [[] for i in range(n)]
  results = []
  last_ans = 0
  for query in queries:
    query_type, x, y = query
    if query_type == 1:
      arr[(x ^ last_ans)%n].append(y)
    else:
      idx = (x ^ last_ans)%n
      last_ans = arr[idx][y%len(arr[idx])]
      results.append(last_ans)
  return results

test_case = (2, [[1,0,5],[1,1,7],[1,0,3],[2,1,0],[2,1,1]])
print(dynamicArray(*test_case))