# Given the head of a linked list, return the list after sorting it in ascending order.

def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
  if not head:
    return

  def sort_helper(runner, length = None):
    # move center node to front if length is known (front node used as pivot). Solves performance issues in initially well sorted lists.
    if length and length > 2:
      runner2 = runner    
      for _ in range(length//2-1):
        runner2 = runner2.next
      front = runner2.next
      runner2.next = runner2.next.next
      front.next = runner
      runner = front

    # three lists: val below pivot, at pivot, and above pivot. New ListNode() used as placeholder in low and high lists, is removed later.
    low_start = ListNode()
    low_end = low_start
    low_len = 0
    pivot_start = runner
    pivot_end = pivot_start
    high_start = ListNode()
    high_end = high_start
    high_len = 0
    while runner.next:
      # iterate through runner list and place nodes in appropriate lists
      runner = runner.next
      if runner.val < pivot_start.val:
        low_end.next = runner
        low_end = low_end.next
        low_len += 1
      elif runner.val == pivot_start.val:
        pivot_end.next = runner
        pivot_end = pivot_end.next
      else:
        high_end.next = runner
        high_end = high_end.next
        high_len += 1
    # after partition, remove residual tails from original list
    low_end.next = None
    high_end.next = None
    pivot_end.next = None
    # remove placeholder nodes in low and high lists
    low_start = low_start.next
    high_start = high_start.next

    # call partition function on low and high lists if there is more than one node
    if low_len > 1:
      low_start, low_end = sort_helper(low_start, length = low_len)
    if high_len > 1:
      high_start, high_end = sort_helper(high_start, length = high_len)
    # stitch low, pivot, and high lists together (depending on which are present)
    if low_len > 0:
      low_end.next = pivot_start
    else:
      low_start = pivot_start
    if high_len > 0:
      pivot_end.next = high_start
    else:
      high_end = pivot_end
    return (low_start, high_end)

  return sort_helper(head)[0]