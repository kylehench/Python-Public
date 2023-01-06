# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.

def hasCycle1(self, head: Optional[ListNode]) -> bool:
  # runner walks through list and adds each node to a set. If a new node is contained in the set, a cycle has been detected.
  if not head:
    return False
  runner = head
  nodes = set([runner])
  while runner.next:
    if runner.next in nodes:
      return True
    nodes.add(runner.next)
    runner = runner.next
  return False

def hasCycle2(self, head: Optional[ListNode]) -> bool:
  # 2 runners walk through the list. 2nd travels twice as fast as the first. If it lands on the same node as the 1st, a cycle has been detected.
  if not head:
    return False
  runner_1 = head
  runner_2 = head
  while runner_2.next and runner_2.next.next:
    runner_2 = runner_2.next.next
    runner_1 = runner_1.next
    if runner_1 == runner_2:
      return True
  return False