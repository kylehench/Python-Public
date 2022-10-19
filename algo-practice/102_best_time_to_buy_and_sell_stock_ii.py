# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
# Find and return the maximum profit you can achieve.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        own = False
        balance = 0
        for a, b in zip(prices, prices[1:]):
            if a<=b and own==False:
                own = True
                balance -= a
            elif a>b and own==True:
                own = False
                balance += a
        if own==True:
            own = False
            balance += prices[-1]
        return balance