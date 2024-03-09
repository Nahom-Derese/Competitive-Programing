from collections import Counter
from math import ceil


n, k = map(int, input().split())
s = list(map(int, input().split()))

x = Counter(s)

m = sorted(x.values(), reverse=True)

ans = float("inf")

for i in range(len(m)-1):
    if m[i] - ceil(k / (i+1)) > m[i+1]:
        ans = min(ans, (m[i] - k, str(x[m[i]]) * i))