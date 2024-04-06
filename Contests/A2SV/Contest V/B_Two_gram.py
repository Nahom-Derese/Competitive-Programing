import sys
from collections import *
from itertools import *
from math import *

def solve(s):
    freq = Counter()
    itr  = 1
    while itr < len(s):
        freq[s[itr-1] + s[itr]]+=1
        itr+=1
    _max = (0, "")
    for k in freq:
        if _max[0] < freq[k]:
            _max = (freq[k], k)
    return _max[1]

n = int(sys.stdin.readline().strip())

s = sys.stdin.readline().strip()

print(solve(s))