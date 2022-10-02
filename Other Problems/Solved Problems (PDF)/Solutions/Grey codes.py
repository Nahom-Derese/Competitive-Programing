x = int(input())

y = [input().split() for i in range(x)]

for i in range(x):
    a,b = y[i]
    a = int(a)
    b = int(b)
    z = ["0" , "1"]
    loop = 0
    while len(z) < 2**a:
        o = list(reversed(z))
        z[:] = map(lambda x: "0"+x, z)
        o[:] = map(lambda x: "1"+x, o)
        z = z + o
        loop += 1
for i in z:    
    print(i)
