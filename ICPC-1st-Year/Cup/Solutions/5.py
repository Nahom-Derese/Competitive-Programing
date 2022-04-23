n = input().split()

a = int(n[0])
b = int(n[1])
c = int(n[2])

d = a + b
e = a * b
v = a - b
r = None
if b!=0:
    r = a / b

if c == d or c == e or c == v or c == r:
    print('true')
else:
    print('false')