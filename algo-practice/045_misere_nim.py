import functools

def misereNim(s):
  if all(x==1 for x in s):
    if len(s)%2==0:
      return 'First'
    else:
      return 'Second'
  return 'Second' if functools.reduce((lambda a,b: a^b),s)==0 else 'First'