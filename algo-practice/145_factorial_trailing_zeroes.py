# Given an integer n, return the number of trailing zeroes in n!.
# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.
# Example 1:
# Input: n = 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
# Example 2:
# Input: n = 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.

def trailingZeroes(self, n: int) -> int:
  # the number of zeroes depends on factors of 2 and 5, since 2*5 == 10 == 1 trailing zero. There is always a surplus of 2s, since every other number is even. Since 5 is the 'limiting factor' (no pun intended), we only need to count 5s.
  divisor = 5
  count_5 = 0
  while divisor <= n:
    # floor division sums each multiple up to n
    count_5 += n//divisor
    # accounts for numbers where 5 can be factored multiple times
    divisor *= 5
  return count_5