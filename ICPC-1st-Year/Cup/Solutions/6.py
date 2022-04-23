n = int(input())

g = input().split()

evens = []
ods = []

for i in range(n):
    g[i] = int(g[i])
    if g[i]%2 == 0:
        evens.append(g[i])
    else:
        ods.append(g[i])

evens.sort()
ods.sort()

ans = evens + ods
st = ""
for i in ans:
    st += str(i) + " "

print(st)