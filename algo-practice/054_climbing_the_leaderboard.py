# An arcade game player wants to climb to the top of the leaderboard and track their ranking. The game uses Dense Ranking, so its leaderboard works like this:

# The player with the highest score is ranked number  on the leaderboard.
# Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.

def climbingLeaderboard(ranked, player):
  ranked = list({x:0 for x in ranked}.keys())
  ranked.reverse()
  ranked_length = len(ranked)
  ranked_i = 0
  player_ranks = []
  for p in player:
    while ranked_i!=ranked_length and ranked[ranked_i]<=p:
      ranked_i += 1
    player_ranks.append(ranked_length-ranked_i+1)
  return player_ranks

test_cases = (
  (([100,90,90,80],
  [70,80,105]),
  [4,3,1]),
  (([100,100,50,40,40,20,10],
  [5,25,50,120]),
  [6,4,2,1]),
  (([100,90,90,80,75,60],
  [50,65,77,90,102]),
  [6,5,4,2,1])
)
for case in test_cases:
  print('PASS') if climbingLeaderboard(*case[0])==case[1] else print('FAIL')