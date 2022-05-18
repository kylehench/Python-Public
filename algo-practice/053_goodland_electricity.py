# Goodland is a country with a number of evenly spaced cities along a line. The distance between adjacent cities is 1 unit. There is an energy infrastructure project planning meeting, and the government needs to know the fewest number of power plants needed to provide electricity to the entire list of cities. Determine that number. If it cannot be done, return -1.

# You are given a list of city data. Cities that may contain a power plant have been labeled 1. Others not suitable for building a plant are labeled 0. Given a distribution range of k, find the lowest number of plants that must be built such that all cities are served. The distribution range limits supply to cities where distance is less than k.

def pylons(k, arr):
  # check if any configuration is possible. Max number of consecutive non-suitable cities (0) is k-1
  # d = 0
  # for city in arr:
  #   if city==0:
  #     d+=1
  #     if d==k: return -1
  #   else: d=0
  # if we have made it here, a configuration is possible. Now optimize number of plants. i is used as an index to find each optimal position, starting from left to right.
  plants = 0
  arr_len = len(arr)
  i_prev = -1
  final_i = arr_len-k # last possible (though not necessarily suitable) position of plant that covers last segment
  i = k-1
  while 1:
    while arr[i]==0:
      i-=1
      if i==i_prev:
        return -1
    plants+=1
    if i>=final_i:
      return plants
    i_prev = i
    i += 2*k-1
    if i>=arr_len:
      i=arr_len-1

test_cases = (
  (3, [0,1,1,1,0,0,0]),
  (2, [0,1,1,1,1,0]),
  (2, [0,1,1,1,1,0]),
  (2, [0,1,0,0,0,1,0, ]),
  (3, [0,1,0,0,0,1,1,1,1,1]),
)
expect = (-1, 2, 2, -1, 3)

for expect, res in zip(expect, [pylons(*case) for case in test_cases]):
  print('Expect: ' + str(expect) + '  Result: ' + str(res))