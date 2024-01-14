n = int(input())
a = list(map(int,input().split()))

infront = 0
for i in range(1,n):
    if a[0] < a[i]:
        infront += 1
    
print(infront)