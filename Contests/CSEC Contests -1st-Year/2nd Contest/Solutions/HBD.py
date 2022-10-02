x = int(input())

y = [input().split() for i in range(x)]
order = {}
for i in y:
    for j in range(4):
        Name = i[0]
        yy = (2021 - int(i[3])) * 365
        mm = (12 - int(i[2])-1)*30
        dd = 30 - int(i[1])
        order[(yy)+(mm)+(dd)] = Name

print(order[min(order)])
print(order[max(order)])

