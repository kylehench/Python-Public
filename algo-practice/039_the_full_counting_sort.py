# Use the counting sort to order a list of strings associated with integers. If two strings are associated with the same integer, they must be printed in their original order, i.e. your sorting algorithm should be stable. There is one other twist: strings in the first half of the array are to be replaced with the character - (dash, ascii 45 decimal).

# Insertion Sort and the simple version of Quicksort are stable, but the faster in-place version of Quicksort is not since it scrambles around elements while sorting.

# Design your counting sort to be stable.

def countSort(arr):
  arr[0:int(len(arr)/2)] = [[e[0], '-'] for e in arr[0:int(len(arr)/2)]]
  int_max = max([int(e[0]) for e in arr])
  new_arr = [[] for _ in range(int_max+1)]
  for i, val in arr:
    new_arr[int(i)].append(val)
  return ' '.join([' '.join(e) for e in new_arr]).strip()

if __name__ == '__main__':
  arr = [['0','ab'],['6','cd'],['0','ef'],['6','gh'],['4','ij'],['0','ab'],['6','cd'],['0','ef'],['6','gh'],['0','ij'],['4','that'],['3','be'],['0','to'],['1','be'],['5','question'],['1','or'],['2','not'],['4','is'],['2','to'],['4','the']]

  print(countSort(arr))