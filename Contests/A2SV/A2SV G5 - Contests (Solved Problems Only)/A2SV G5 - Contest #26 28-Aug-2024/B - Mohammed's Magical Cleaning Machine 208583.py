# Problem: B - Mohammed's Magical Cleaning Machine - https://codeforces.com/gym/537362/problem/B

for _ in range(int(input())):
    n = int(input())
    dust_levels = list(map(int, input().split()))

    max_ops = 0 
    for dust in dust_levels[:-1]:
        if dust or max_ops > dust:
            max_ops += dust + int(dust == 0)

    print(max_ops)