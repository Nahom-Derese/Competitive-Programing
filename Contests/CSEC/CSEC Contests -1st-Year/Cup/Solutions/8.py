n = int(input())

s = input().split()

st = ""
a = 0
b = 0
c = 0

for i in s:
    a += int(i[0])
    b += int(i[1])
    c += int(i[2])

st = str(a) + " " + str(b) + " " + str(c)

print(st)