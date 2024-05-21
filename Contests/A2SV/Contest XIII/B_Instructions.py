import sys
import threading


def main():
    def solve():
        n = int(sys.stdin.readline().strip())
        nums = [int(i) for i in sys.stdin.readline().split()]

        mem = {}

        def rec(idx):
            if idx in mem:
                return mem[idx]
            if idx > n:
                return 0

            res = rec(idx+nums[idx-1]) + nums[idx-1]
            mem[idx] = res
            return res

        ans = 0
        for i in range(n):
            ans = max(ans, rec(i+1))

        print(ans)

    for _ in range(int(input())):
        solve()


if __name__ == '__main__':

    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)
    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
