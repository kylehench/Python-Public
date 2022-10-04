# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.
# A substring is a contiguous sequence of characters within the string.

class Solution:
  def minWindow(self, s: str, t: str) -> str:
    t_len = len(t)
    
    # increment down as matches in string are found. value of 0 indicates valid substring
    t_delta = t_len
    
    letter_set = set(t)
    # indexes of letters found in string
    letter_idxs = {ch: [] for ch in letter_set}
    
    # dictionary - character: required count of character
    letter_count = {ch: 0 for ch in letter_set}
    for ch in t:
      letter_count[ch] += 1
        
    min_substring_len = 10**6
    min_substring_idxs = None
    
    # two pointer solution
    i, i_ch = 0, s[0]
    for j, ch in enumerate(s):
      # if letter is in set, append index to letter index dictionary
      if ch in letter_set:
        if t_delta > 0 and len(letter_idxs[ch]) < letter_count[ch]:
          t_delta -= 1
        letter_idxs[ch].append(j)
          
      # increment left pointer if pointer value not in set, or excess indexes in letter index dictionary
      while i < len(s) and (i_ch not in letter_set or len(letter_idxs[i_ch]) > letter_count[i_ch]):
        if i_ch in letter_set:
          letter_idxs[i_ch] = letter_idxs[i_ch][1:]
        if i == len(s)-1:
          break
        i += 1
        i_ch = s[i]
          
      # save substring indexes if they contain all letters in t and represent current minimum
      substring_len = j-i+1
      if t_delta == 0 and substring_len < min_substring_len:
        min_substring_len = substring_len
        min_substring_idxs = (i, j)
    if min_substring_idxs == None:
      return ''
    else:
      return s[min_substring_idxs[0]:min_substring_idxs[1]+1]