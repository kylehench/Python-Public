# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

def titleToNumber(self, columnTitle: str) -> int:
  factor = 1
  col = 0
  offset = ord('A')-1
  for ch in columnTitle[::-1]:
    col += factor * (ord(ch)-offset)
    factor *= 26
  return col