import sys
from collections import *
from itertools import *
from math import *


n = int(sys.stdin.readline().strip())

s = sys.stdin.readline().strip()

vowels = set("aeiouy")
ans = ""
r = 0
while r < n:
    c = s[r]
    ans += c

    if c in vowels:
        while r < n and s[r] in vowels:
            r += 1
    else:
        r += 1


print(ans)
