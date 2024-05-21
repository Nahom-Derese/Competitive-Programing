import sys
import threading
from collections import *
from itertools import *
from math import *


def main():
    n, a, b, c = [int(i) for i in sys.stdin.readline().split()]

    mem = {}

    def dp(tot):
        if tot in mem:
            return mem[tot]

        if tot == 0:
            return 1

        res = 0
        for i in [a, b, c]:
            if tot-i >= 0:
                p = dp(tot-i)
                if p:
                    res = max(res, p+1)

        mem[tot] = res
        return res
    ans = dp(n)-1
    print(ans)


if __name__ == '__main__':

    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
