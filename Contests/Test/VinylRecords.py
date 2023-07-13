import math

i = input()

j = [int(x) for x in input().split()]

if (len(j) == 1):
    print(round(math.pi, 6))
    exit()

j.sort()
j.reverse()

ans = 0

for i in range(0, len(j), 2):
    if (len(j)-1 == i):
        ans += j[i]**2
        break
    ans += j[i]**2 - j[i+1]**2

print(round(ans*math.pi, 6))
