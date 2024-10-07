a, b = [int(i) for i in input().split()]

A = B = Draw = 0

for num in range(1, 7):
    x = abs(num - a)
    y = abs(num - b)

    Draw += x == y
    A += x < y
    B += x > y

print(A, Draw, B)