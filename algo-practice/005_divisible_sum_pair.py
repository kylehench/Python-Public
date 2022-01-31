import sys

# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar


def divisibleSumPairs(n, k, ar):
    rest = [0] * k
    pairs_count = 0
    for elem in ar:
        pairs_count += rest[(k - elem % k) % k]
        rest[elem % k] += 1
    return pairs_count

#O(N^2) solution
def divisibleSumPairs1(n, k, ar):
    count = 0
    for i, num1 in enumerate(ar[:-1]):
        count += sum([1 for num2 in ar[i+1:] if (num1+num2)%k==0])
    return count

if __name__ == '__main__':
    if 0:
        fptr = sys.stdout
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])
        ar = list(map(int, input().rstrip().split()))
        result = divisibleSumPairs(n, k, ar)
        fptr.write(str(result) + '\n')
        fptr.close()
    
    else:
        n = 6
        k = 3
        ar = [1, 3, 2, 6, 1, 2]
        print(divisibleSumPairs(n, k, ar))