# Problem: C. Given Length and Sum of Digits... - https://codeforces.com/contest/489/problem/C

import sys
from collections import *
from itertools import *
from math import *


m, s = [int(i) for i in sys.stdin.readline().split()]

max_ = []
min_ = []

while s:
    if s >= 9:
        s -= 9
        max_.append("9")
    else:
        max_.append(str(s))
        s = 0

max_.extend((["0"] * (m - len(max_))))

min_ = max_[::-1]

if min_[0] == "0":
    itr = 1
    while itr < len(min_) and min_[itr] == "0":
        itr += 1

    if itr < len(min_):
        min_[itr] = str(int(min_[itr])-1)
        min_[0] = "1"

max_ = int("".join(max_))
min_ = int("".join(min_))

digits_max = len(str(max_))
digits_min = len(str(min_))

if (digits_max == digits_min == m):
    print(min_, max_)
else:
    print(-1, -1)
