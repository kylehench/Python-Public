class Solution:
  def strStr(self, haystack: str, needle: str) -> int:
    ch_0 = needle[0]
    if len(needle) > len(haystack): return -1
    for i, ch in enumerate(haystack[:len(haystack)-len(needle)+1]):
      if ch_0==ch:
        matching = True
        for j in range(1, len(needle)):
          if haystack[i+j] != needle[j]:
            matching = False
            break
        if matching:
          return i
    return -1