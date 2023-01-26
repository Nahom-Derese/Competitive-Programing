from math import *
from itertools import combinations_with_replacement
word = int(input())

a = ceil(log2(word))

print(list(combinations_with_replacement('47', 3)))
