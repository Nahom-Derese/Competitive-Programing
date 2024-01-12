sum_A = 0
sum_B = 0
sum_C = 0
for i in range(int(input())):
    a, b, c = [int(x) for x in input().split()]
    sum_A+=a
    sum_B+=b
    sum_C+=c

if sum_A == 0 and sum_B == 0 and sum_C == 0:
    print("YES")
else:
    print("NO")