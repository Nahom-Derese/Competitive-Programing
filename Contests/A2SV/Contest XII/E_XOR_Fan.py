import sys
from collections import *
from itertools import *
from math import *
import operator


for _ in range(int(input())):
    n = int(sys.stdin.readline().strip())
    nums = [int(i) for i in sys.stdin.readline().split()]
    bits = list(sys.stdin.readline().strip())
    prefix_xor = [0] + list(accumulate(nums, operator.xor))

    ones = 0
    zeroes = 0

    for i, bit in enumerate(bits):
        if bit == "1":
            ones ^= nums[i]
        else:
            zeroes ^= nums[i]

    for _ in range(int(input())):
        query = [int(i) for i in sys.stdin.readline().split()]
        if query[0] == 1:
            l = query[1]-1
            r = query[2]

            range_value = prefix_xor[r] ^ prefix_xor[l]

            ones ^= range_value
            zeroes ^= range_value

        else:
            if query[1]:
                print(ones, end=" ")
            else:
                print(zeroes, end=" ")
    print()
