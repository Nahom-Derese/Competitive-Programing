from itertools import accumulate
from bisect import *

try:
    for i in range(int(input())):
        worms = [int(i) for i in input().split()]
        pre_sum = list(accumulate(worms))

        q = int(input())

        queries = [int(i) for i in input().split()]
        for q in queries:
            print(bisect_left(pre_sum, q) + 1)
except:
    pass