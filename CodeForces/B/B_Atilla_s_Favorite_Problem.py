for i in range(int(input())):
    n = int(input())

    _max = 0
    for i in input():
        x = ord(i)
        _max = max(_max, x)

    print(_max - ord('a') + 1)