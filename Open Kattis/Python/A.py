a = int(input())

b = [int(i) for i in input().split()]

c = set(b)

summation = sum(b)

ans = []

for i in c:
    b.remove(i)
    ans.append(str(summation - i))
    b.append(i)

ans.sort()

print(len(c))

print(" ".join(ans))