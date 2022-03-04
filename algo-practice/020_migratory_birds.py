# Given an array of bird sightings where every element represents a bird type id, determine the id of the most frequently sighted type. If more than 1 type has been spotted that maximum amount, return the smallest of their ids.

def migratoryBirds(arr):
  bird_count = {}
  for id in arr:
    if id not in bird_count:
      bird_count[id] = 1
    else:
      bird_count[id] += 1
  max_count_value = max(bird_count.values())
  max_count_ids = []
  for id, count in bird_count.items():
    if count==max_count_value:
      max_count_ids.append(id)
  max_count_ids.sort()
  return max_count_ids[0]

test_case = [1,1,2,2,3] # answer is 1
print(migratoryBirds(test_case))