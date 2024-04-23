import sys
import string
from collections import *
from itertools import *
from math import *
from bisect import *

def corrected_alphabet(orders):
    pass

orders = []
for i in range(int(input())):
    orders.append(input())


alp = set(["r","s","a"])

print(*[i for i in string.ascii_lowercase[:bisect_right(string.ascii_lowercase, "r")] if i not in alp])
