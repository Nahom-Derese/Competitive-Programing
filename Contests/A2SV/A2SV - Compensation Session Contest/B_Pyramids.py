from bisect import *

n = int(input())


def prefix_sum(arr):
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = prefix[i - 1] + arr[i]
    return prefix


summation = prefix_sum(list(range(10000)))
sum_summation = prefix_sum(summation)

x = bisect_right(sum_summation, n)
print(x-1)