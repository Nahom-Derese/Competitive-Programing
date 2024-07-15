from math import factorial

n, m, t = [int(i) for i in input().split()]

fact1 = factorial(n)
fact2 = factorial(m)

possible_ways = []
ans = 0
for b in range(4, n+5):
    for g in range(1, m+5):
        if b+g == t:
            possible_ways.append((b, g))


def combination(a, b):
    comb1 = fact1 / (factorial(n - a) * factorial(a))
    comb2 = fact2 / (factorial(m - b) * factorial(b))
    
    return comb1 * comb2

for boys, girls in possible_ways:
    ans += combination(boys, girls)

print(int(ans))