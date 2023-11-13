import math

a = int(input())

answer = []

for i in range(a):
    b = int(input())

    finalx = 0
    finaly = 0

    for j in range(b):
        angle, distance = [float(k) for k in input().split()]
        rad = math.radians(angle) + math.radians(90)
        x = math.cos(rad) * distance
        y = math.sin(rad) * distance
        
        finalx += x
        finaly += y

    answer.append([finalx,finaly])

for i in answer:
    for j in i:
        print("{:.3f}".format(j), end=" ")
    print()