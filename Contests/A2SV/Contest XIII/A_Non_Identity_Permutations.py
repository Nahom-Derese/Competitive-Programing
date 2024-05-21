import sys
# import threading


def main():
    def solve():
        n = int(sys.stdin.readline().strip())

        x = list(range(1, n + 1))
        x.append(x.pop(0))
        return x

    for _ in range(int(input())):
        print(*solve())


if __name__ == '__main__':
    main()