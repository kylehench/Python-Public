# Given a string, return its encoding defined as follows:

# First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
# for example, "aabbbc" is divided into ["aa", "bbb", "c"]
# Next, each substring with length greater than one is replaced with a concatenation of its length and the repeating character
# for example, substring "bbb" is replaced by "3b"
# Finally, all the new strings are concatenated together in the same order and a new string is returned.

def solution(s):
  groups = [s[0]]
  for a, b in zip(s[:-1], s[1:]):
    if a==b:
      groups[-1] += b
    else:
      groups.append(b)
  for i in range(len(groups)):
    if len(groups[i]) > 1:
      groups[i] = str(len(groups[i])) + groups[i][0]
  return ''.join(groups)
        
