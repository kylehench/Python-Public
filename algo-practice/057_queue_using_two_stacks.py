# A queue is an abstract data type that maintains the order in which elements were added to it, allowing the oldest elements to be removed from the front and new elements to be added to the rear. This is called a First-In-First-Out (FIFO) data structure because the first element added to the queue (i.e., the one that has been waiting the longest) is always the first one to be removed.

# A basic queue has the following operations:

# Enqueue: add a new element to the end of the queue.
# Dequeue: remove the element from the front of the queue and return it.
# In this challenge, you must first implement a queue using two stacks. Then process q queries, where each query is one of the following 3 types:

# 1 x: Enqueue element x into the end of the queue.
# 2: Dequeue the element at the front of the queue.
# 3: Print the element at the front of the queue.

import os

# note: this challenge involves FIFO operations, which can be very slow when using a list structure with a large number of items. For lists in Python, .append() is fast, but del arr[i] is slow. Instead of deleting front itmes, an index can be used to mark the start of the list.

if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')
  query_count = int(input().strip())
  que = []
  start_idx = 0
  
  for _ in range(query_count):
    arr = list(map(int, input().rstrip().split()))
    query_type = arr[0]
    if query_type==1:
      que.append(arr[1])
    elif query_type==2:
      start_idx+=1
    elif query_type==3:
      fptr.write(str(que[start_idx])+ '\n')
  fptr.close()
