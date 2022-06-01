# Chief's bot is playing an old DOS based game. There is a row of buildings of different heights arranged at each index along a number line. The bot starts at building 0 and at a height of 0. You must determine the minimum energy his bot needs at the start so that he can jump to the top of each building without his energy going below zero.

# Units of height relate directly to units of energy. The bot's energy level is calculated as follows:
# newEnergy = 2 * botEnergy - height

import math
from timeit import timeit

def chiefHopper1(arr):
  # end with an energy level of 0 in ideal case. Work backwards to ensure minimum energy level at all locations. Only integers allowed.
  # newEnergy = 2 * botEnergy - height
  # [rename] Energy = 2 * prevEnergy - height
  # prevEnergy = (Energy + height)/2
  botEnergy = 0
  for x in arr[::-1]:
    botEnergy = int((botEnergy-(1e-9) + x)/2)+1
  return botEnergy


def chiefHopper2(arr):
  # end with an energy level of 0 in ideal case. Work backwards to ensure minimum energy level at all locations. Only integers allowed.
  # newEnergy = 2 * botEnergy - height
  # [rename] Energy = 2 * prevEnergy - height
  # prevEnergy = (Energy + height)/2
  botEnergy = 0
  for x in arr[::-1]:
    botEnergy = math.ceil((botEnergy + x)/2)
  return botEnergy

test_cases = ([3,4,3,2,4],[4,4,4],[1,6,4])
test_results = (3,4,4)

if sum(chiefHopper1(case)==result for case, result in zip(test_cases, test_results))==0:
  print('chiefHopper1 PASSES all tests.')
if sum(chiefHopper2(case)==result for case, result in zip(test_cases, test_results))==0:
  print('chiefHopper2 PASSES all tests.')


number = 100000
print(sum(timeit(lambda: chiefHopper1(case), number=number) for case in test_cases))
print(sum(timeit(lambda: chiefHopper2(case), number=number) for case in test_cases))