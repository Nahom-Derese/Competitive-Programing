import sys
from collections import *
from itertools import *
from heapq import *


for i in range(int(input())):
    n = int(sys.stdin.readline().strip())
    
    nums = [int(i) for i in sys.stdin.readline().split()]

    heap = []

    ans = 0
    for i in nums:
        if not i:
            if heap:
                ans+= -heappop(heap)
        else:
            heappush(heap, -i)

    print(ans)