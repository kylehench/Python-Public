# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

class Solution:
  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    prev_start = intervals[0][0]
    prev_end = intervals[0][1]
    res = []
    for start, end in intervals[1:]:
      if start <= prev_end:
        prev_end = max(prev_end, end)
      else:
        res.append([prev_start, prev_end])
        prev_start = start
        prev_end = end
    res.append([prev_start, prev_end])
    return res