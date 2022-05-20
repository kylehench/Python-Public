# Two friends like to pool their money and go to the ice cream parlor. They always choose two distinct flavors and they spend all of their money.
# Given a list of prices for the flavors of ice cream, select the two that will cost all of the money they have.
# Example: m=6, cost=[1,3,4,5,6]
# The two flavors that cost 1 and 5 meet the criteria. Using 1-based indexing, they are at indices 1 and 4.

def icecreamParlor(m, arr):
  pricesDict = {price:i for i, price in enumerate(arr)}
  for i in range(len(arr)):
    if m-arr[i] in pricesDict:
      if arr[i]==m/2 and sum([x==m/2 for x in arr])!=2:
        continue
      return [i+1, pricesDict[m-arr[i]]+1]