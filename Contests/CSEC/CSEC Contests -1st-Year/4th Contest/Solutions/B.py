from math import *
from typing import cast
ts = int(input())

ans = []
for i in range(ts):
    n = int(input())
    a = input().split()
    hi = 0
    lo = 0
    for j in range(n):
        a[j] = int(a[j])
    for k in range(n-1):
        if a[k+1] > a[k]:
            hi += 1
        elif a[k+1] < a[k]:
            lo += 1
    ans.append([hi,lo])

for l in range(len(ans)):
    print("Case {0}: {1} {2}".format(l,ans[l][0],ans[l][1]))