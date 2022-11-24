# A media access control address (MAC address) is a unique identifier assigned to network interfaces for communications on the physical network segment.

# The standard (IEEE 802) format for printing MAC-48 addresses in human-friendly form is six groups of two hexadecimal digits (0 to 9 or A to F), separated by hyphens (e.g. 01-23-45-67-89-AB).

# Your task is to check by given string inputString whether it corresponds to MAC-48 address or not.

def solution(inputString):
  if len(inputString) != 17:
    return False
  if any(inputString[i]!='-' for i in range(2,15,3)):
    return False
  for i in range(12):
    ch = inputString[3*int(i/2) + i%2]
    if not (ch.isnumeric() or 65 <= ord(ch) <= 70):
      return False
  return True