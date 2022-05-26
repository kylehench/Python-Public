# Your algorithms have become so good at predicting the market that you now know what the share price of Wooden Orange Toothpicks Inc. (WOT) will be for the next number of days.

# Each day, you can either buy one share of WOT, sell any number of shares of WOT that you own, or not make any transaction at all. What is the maximum profit you can obtain with an optimum trading strategy?

# Notes: The strategy is to buy as many shares as you can before the maximum share price. This may occur several times as the stock price fluctuates.

def stockmax(prices):
  if len(prices)==1:
    return 0
  sell_idxs = []
  maximum = 0
  # Starting from the end of prices and iterating in reverse, save index of each consecutive maximum 
  for i in range(len(prices)-1,-1,-1):
    if prices[i] > maximum:
      maximum = prices[i]
      sell_idxs.append(i)
  sell_idxs.reverse() # reverse sell days for foward iteration
  profit = 0
  last_sell_idx = -1
  for i in sell_idxs:
    # add sales of each sale date to profit: number of days(i.e. 1 stock purchaches/day available to sell)*stock price - purchase price of those stocks
    profit += (i-last_sell_idx-1)*prices[i]-sum(prices[last_sell_idx+1:i])
    last_sell_idx = i
  return profit

test_cases = ((5,3,2),(1,2,100),(1,3,1,2))
for case in test_cases:
  print(stockmax(case))