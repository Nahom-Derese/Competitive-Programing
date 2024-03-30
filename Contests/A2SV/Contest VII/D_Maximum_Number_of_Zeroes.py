import sys
from collections import *
from itertools import *
from math import *
from fractions import Fraction


n = int(sys.stdin.readline().strip())

nums1 = [int(i) for i in sys.stdin.readline().split()]
nums2 =  [int(i) for i in sys.stdin.readline().split()]

divs = []
extra = ans = 0
for i in range(n):
    if nums1[i] and nums2[i]:
        divs.append(Fraction(nums1[i], nums2[i]))
    elif not nums1[i] and not nums2[i]:
        extra+=1

count = Counter(divs)
for i in count:
    ans = max(count[i]+extra, ans)
ans = max(ans, nums2.count(0))

print(ans)