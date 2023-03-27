a = int(input())

b = [int(i) for i in input().split()]

c = [int(i) for i in input().split()]

for j in b:
    if j in c:
        continue
    else:
        print(j)