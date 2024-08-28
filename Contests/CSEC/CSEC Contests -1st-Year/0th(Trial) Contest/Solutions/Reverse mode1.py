inp = int(input())

a = input().split()

for i in range(len(a)):
    a[i] = int(a[i])

ans = a[0] + (a[1]-a[0]) * (inp)

print(ans)