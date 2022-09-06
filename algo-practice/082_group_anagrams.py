# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    strs = sorted([(''.join(sorted(item)), item) for item in strs])
    word_s_prev, word_prev = strs[0]
    res = []
    group = [word_prev]
    for word_s, word in strs[1:]:
      if word_s == word_s_prev:
        group.append(word)
      else:
        res.append(group)
        word_s_prev = word_s
        group = [word]
    res.append(group)
    return res