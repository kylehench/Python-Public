# Implement a simple text editor. The editor initially contains an empty string, s. Perform q operations of the following 4 types:

# append w - Append string w to the end of s.
# delete k - Delete the last k characters of s.
# print k - Print the kth character of s.
# undo - Undo the last (not previously undone) operation of type 1 or 2, reverting s to the state it was in prior to that operation.


# Enter your code here. Read input from STDIN. Print output to STDOUT
import os
fptr = open(os.environ['OUTPUT_PATH'], 'w')

q = int(input())
s = []
undo_stack = []
for _ in range(q):
  command = list(input().strip().split())
  undo = False
  if command[0] == '4':
    # undo operation
    undo = True
    command = undo_stack.pop()
  command_type = command[0]
  if command_type == '1':
    # append characters
    s.extend(list(command[1]))
    if not undo:
      undo_stack.append(['2', len(command[1])])
  elif command_type == '2':
    # delete characters
    delete_count = int(command[1])
    if not undo:
      undo_stack.append(['1', ''.join(s[-delete_count:])])
    del s[-delete_count:]
  elif command_type == '3':
    # print character
    fptr.write(s[int(command[1])-1]+'\n')
fptr.close()