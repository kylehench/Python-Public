# given a list on integers, return the sum of the concatenated combinations of every integer
# example [11, 5] --> 1111 + 115 + 55 + 511 = 1792

def sum_concat_integers(arr):
    arr_len = len(arr)
    arr_strings = [str(integer) for integer in arr]
    arr_lengths = [len(string) for string in arr_strings]
    lengths_count = [0 for _ in range(max(arr_lengths)+1)]
    for x in arr_lengths:
        lengths_count[x] += 1
    res = sum(integer*arr_len for integer in arr)
    for string in arr_strings:
        res += sum(int(string + '0'*i)*count for i, count in enumerate(lengths_count))
    return res


test_cases = ([11,5],[11,5,980])
for test_case in test_cases:
    print(sum_concat_integers(test_case))