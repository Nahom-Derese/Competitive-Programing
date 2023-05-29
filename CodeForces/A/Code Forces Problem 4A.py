weight = int(input())

# check if the weight can be divided into two even parts
if weight % 2 == 0 and weight > 2:
    print("YES")
else:
    print("NO")