# Problem: Raising Bacteria - https://codeforces.com/contest/579/problem/A

import sys

x = int(sys.stdin.readline().strip())
ans = 0
while x:
    ans += x & 1
    x >>= 1
print(ans)
