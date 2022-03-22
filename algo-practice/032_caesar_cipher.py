def caesarCipher(s, k):
  lower_start = ord('a')
  upper_start = ord('A')
  new_string = ''
  for char in s:
    if char.isalpha():
      if ord(char) < lower_start:
        # char is upper
        new_string += chr((ord(char)-upper_start+k)%26+upper_start)
      else:
        new_string += chr((ord(char)-lower_start+k)%26+lower_start)
    else:
      new_string += char
  return new_string

test_case = ("There's-a-starman", 3)
print(caesarCipher(*test_case))