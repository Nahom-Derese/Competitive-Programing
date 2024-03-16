from itertools import accumulate
from bisect import *

s, b = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

defense_gold = [[int(i) for i in input().split()] for _ in range(b)]
defense_gold.sort(key=lambda x: x[0])

pre_sum_gold = [0] +list(accumulate(map(lambda x: x[1], defense_gold)))
defense = list(map(lambda x: x[0], defense_gold))

for i in a:
    print(pre_sum_gold[bisect_right(defense, i)], end=" ")
