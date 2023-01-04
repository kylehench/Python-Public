# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.

def wordBreak(self, s: str, wordDict: List[str]) -> bool:
  # records whether segments ending at index are valid
  passes = [True] + [False] * len(s)
  for i in range(1, len(s)+1):
    for word in wordDict:
      if len(word) > i:
        continue
      if passes[i-len(word)] and s[i-len(word):i]==word:
        passes[i] = True
  return passes[-1]