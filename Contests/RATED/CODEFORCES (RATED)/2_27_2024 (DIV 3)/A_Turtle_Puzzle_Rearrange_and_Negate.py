for i in range(int(input())):
    n = int(input())

    print(sum(map(lambda i: abs(int(i)), input().split())))