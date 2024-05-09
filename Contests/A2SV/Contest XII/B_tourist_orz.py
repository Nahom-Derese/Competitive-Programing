import sys
from collections import *
from itertools import *
from math import *


for i in range(int(input())):
    n, z = [int(i) for i in sys.stdin.readline().split()]
    nums = [int(i) | z for i in sys.stdin.readline().split()]

    print(max(nums))
