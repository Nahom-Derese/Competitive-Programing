x = True
while(x):
    z = input()
    if (z == "0"):
        x = False
    else:
        list = []
        areas = 0
        for i in range(int(z)):
            a,b,c,d = [int(y) for y in input().split()]
            list.append([a,b],[c,d])
            areas += (c-a) * (d-b)
        
        for j in list:
            pass