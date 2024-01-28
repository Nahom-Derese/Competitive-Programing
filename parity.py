g = int(input())
a = [int(i) for i in input().split()]

y = [i for i in a if a%2==0].sort()
u = [i for i in a if not a%2==0].sort()
s = y+u
print(*s)