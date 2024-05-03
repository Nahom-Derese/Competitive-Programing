import sys
from collections import *
from itertools import *
from math import *


for i in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    if n < k:
        print(n)
        continue
    else:
        counts = defaultdict(int)
        for num in a:
            counts[num] +=  1
            if counts[num] >= k:
                print(k-1)
                break
        else:
            print(n)