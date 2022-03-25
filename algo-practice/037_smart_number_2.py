from cgi import test
import math

# In this challenge, the task is to debug the existing code to successfully execute all provided test files.
# A number is called a smart number if it has an odd number of factors. Given some numbers, find whether they are smart numbers or not.
# Debug the given function is_smart_number to correctly check if a given number is a smart number.
# Note: You can modify only one line in the given code and you cannot add or remove any new lines.
# To restore the original code, click on the icon to the right of the language selector.
# Input Format
# The first line of the input contains t, the number of test cases.
# The next t lines contain one integer each.

def is_smart_number(num):
  val = int(math.sqrt(num))
  if num / val == val:
    return True
  return False


test_cases = (1,2,7,169)

for num in test_cases:
  ans = is_smart_number(num)
  if ans:
    print("YES")
  else:
    print("NO")