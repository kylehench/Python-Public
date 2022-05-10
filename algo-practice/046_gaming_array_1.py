# Andy wants to play a game with his little brother, Bob. The game starts with an array of distinct integers and the rules are as follows:

# Bob always plays first.
# In a single move, a player chooses the maximum element in the array. He removes it and all elements to its right. For example, if the starting array arr = [2,3,5,4,1], then it becomes arr' = [2,3] after removing [5,4,1].
# The two players alternate turns.
# The last player who can make a move wins.
# Andy and Bob play g games. Given the initial array for each game, find and print the name of the winner on a new line. If Andy wins, print ANDY; if Bob wins, print BOB.

# To continue the example above, in the next move Andy will remove 3. Bob will then remove 2 and win because there are no more integers to remove.

def gamingArray(arr):
  count = 0
  max = 0
  for x in arr:
    if x > max:
      max = x
      count += 1
  if count%2 != 0:
    return 'BOB'
  else:
    return 'ANDY'

test = [2,3,5,4,1]
print(gamingArray(test))