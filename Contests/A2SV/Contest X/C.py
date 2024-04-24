import sys
from collections import *
from itertools import *
from math import *

k,d,t = map(int,input().split())

if k > d:
    off_time = (d * ceil(k / d)) % k
else:
    off_time = d - k

on_time = k
one_round = on_time + off_time / 2

rounds, remainder = divmod(t, one_round)

ans = rounds * (on_time + off_time)
if(remainder > on_time):
    ans+=on_time + (remainder - on_time)*2
else:
    ans+=remainder

print(ans)