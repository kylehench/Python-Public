
#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly  steps, for every step it was noted if it was an uphill, , or a downhill,  step. Hikes always start and end at sea level, and each step up or down represents a  unit change in altitude. We define the following terms:

# A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
# A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
# Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.

def countingValleys(steps, path):
  prev_elevation = 0
  elevation = 0
  valley_count = 0
  for direction in path:
    prev_elevation = elevation
    if direction == 'D':
      elevation -= 1
    else:
      elevation += 1
    if elevation == 0 and prev_elevation == -1:
      valley_count += 1
  return valley_count

if __name__ == '__main__':
  steps = 8

  path = 'UDDDUDUU'

  result = countingValleys(steps, path)

  print(result)
