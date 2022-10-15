# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    maximum = prices[-1]
    max_arr = [maximum]
    for i in range(len(prices)-2, -1, -1):
      if prices[i] > maximum:
        maximum = prices[i]
      max_arr.append(maximum)  
    max_arr.reverse()
    
    max_profit = 0
    minimum = prices[0]
    for i in range(len(prices)):
      if prices[i] < minimum:
        minimum = prices[i]
      if max_arr[i]-minimum > max_profit:
        max_profit = max_arr[i]-minimum
    return max_profit