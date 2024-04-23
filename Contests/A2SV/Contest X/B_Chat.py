import sys
from heapq import *

n, k, q = [int(i) for i in sys.stdin.readline().split()]

freindship = [int(i) for i in sys.stdin.readline().split()]

top_k_friends = []

for i in range(q):
    c, _id = [int(i) for i in sys.stdin.readline().split()]
    
    if c == 1:
        if len(top_k_friends) < k:
            heappush(top_k_friends,(freindship[_id-1], _id))
        elif top_k_friends and freindship[_id-1] > top_k_friends[0][0]:
            heappushpop(top_k_friends,(freindship[_id-1], _id))
    else:
        if _id in set([i[1] for i in top_k_friends]):
            print("YES")
        else:
            print("NO")