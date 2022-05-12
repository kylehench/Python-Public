# Louise and Richard have developed a numbers game. They pick a number and check to see if it is a power of 2. If it is, they divide it by 2. If not, they reduce it by the next lower number which is a power of 2. Whoever reduces the number to 1 wins the game. Louise always starts.
# Given an initial value, determine who wins the game.
# Example
# It's Louise's turn first. She determines that 123 is not a power of 2. The next lower power of 2 is 128, so she subtracts that from 132 and passes 4 to Richard. 4 is a power of 2, so Richard divides it by 2 and passes 2 to Louise. Likewise, 2 is a power so she divides it by 2 and reaches 1. She wins the game.
# Update If they initially set counter to 1, Richard wins. Louise cannot make a move so she loses.
#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#


def counterGame(n):
  count = 0
  while n != 1:
    count += 1
    lower_power = 2
    while lower_power <= n/2:
      lower_power = lower_power*2
    if lower_power == n:
      n = int(n/2)
    else:
      n = n - lower_power
  return 'Richard' if count%2 == 0 else 'Louise'

test_cases = (132, 1, 6)
for test in test_cases:
  print(counterGame(test))