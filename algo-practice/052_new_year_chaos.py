# It is New Year's Day and people are in line for the Wonderland rollercoaster ride. Each person wears a sticker indicating their initial position in the queue from 1 to n. Any person can bribe the person directly in front of them to swap positions, but they still wear their original sticker. One person can bribe at most two others.

# Determine the minimum number of bribes that took place to get to a given queue order. Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.
    
def minimumBribes(q):
  # iterate through positions 0:-2 in the que and count swaps required from initial que. Only need to compare with 2 positions ahead because max number of bribes for individual is 2.
  bribes = 0
  x0, x1 = 1, 2
  for i, desired in enumerate(q[0:-2]):
    x2 = i+3
    if desired==x0:
      x0, x1 = x1, x2
    elif desired==x1:
      bribes += 1
      x1 = x2
    elif desired==x2:
      bribes += 2
    else:
      print('Too chaotic')
      return
  # determine if final swap is needed
  if q[-2]!=x0:
    bribes += 1
  print(bribes)
    

test_cases = (
  [1,2,3,5,4,6,7,8],
  [4,1,2,3],
  [2,1,5,3,4],
  [2,5,1,3,4],
  [1,2,5,3,7,8,6,4],
)
# 1, Too chaotic, 3, Too chaotic, 7

for test in test_cases:
  minimumBribes(test)