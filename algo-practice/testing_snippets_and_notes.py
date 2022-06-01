# hard-coded input
test_cases = ('',)
test_results = (1,)

# system I/O
import os
fptr = open(os.environ['OUTPUT_PATH'], 'w')
# input one line
line = input().strip()
# input one line split into array
arr = list(map(int, input().rstrip().split()))
# output one line
fptr.write('output')
fptr.close()

# local file input
with open(r"file_path") as f:
  test_cases = f.readlines()
with open(r"file_path") as f:
  test_results = f.readlines()
test_cases = [s.strip() for s in test_cases[1:]]
test_results = [s.strip() for s in test_results]

# test
all_pass = True
for i, (case, result) in enumerate(zip(test_cases, test_results)):
  my_result = function(case)
  if  my_result != result:
    all_pass = False
    print(f'FAIL. My result: {my_result}. Expected result: {result}. Index: {i}')
if all_pass == True:
  print('ALL PASS')

# timeit
from timeit import timeit 
number = 1000
print(timeit(lambda: function(case), number=number))