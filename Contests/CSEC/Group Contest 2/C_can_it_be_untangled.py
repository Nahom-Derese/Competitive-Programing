import sys
from collections import *
from itertools import *
from math import *


s=input()
stack = []
for st in s:
    if stack and stack[-1]==st:
        stack.pop()
        continue
    stack.append(st)
if stack:
    print("No")
else:
    print("Yes")