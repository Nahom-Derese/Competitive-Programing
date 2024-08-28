import sys
from collections import *
from itertools import *
from math import *


rows = int(sys.stdin.readline().strip())
widths = [(int(x),i)  for i, x in enumerate(sys.stdin.readline().split())]
people = sys.stdin.readline().strip()

# print(widths)
widths.sort(reverse=True)

stack = []
ans = []

for i in range(len(people)):
    if people[i] == "0":
        x, y = widths.pop()
        stack.append((x,y))
        ans.append(y+1)
    else:
        x, y = stack.pop()
        ans.append(y+1)
        
print(*ans)