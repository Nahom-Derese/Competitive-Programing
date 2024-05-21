import sys
import threading
import sys
from collections import *
from itertools import *
from math import *


def main():
    n = int(sys.stdin.readline().strip())
    nums = [int(i) for i in sys.stdin.readline().split()]
    count = Counter(nums)
    

    u = list(count.keys())
    u.sort()

    mem = {}

    def dp(idx):
        if idx in mem:
            return mem[idx]
        if idx >= len(u):
            return 0

        res = dp(idx+1)

        num = u[idx]

        if idx+1 < len(u) and u[idx+1] == num+1:
            res = max((count[num] * num) + dp(idx+2), res)
        else:
            res = max((count[num] * num) + dp(idx+1), res)

        mem[idx] = res
        return res

    print(dp(0))


if __name__ == '__main__':

    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
