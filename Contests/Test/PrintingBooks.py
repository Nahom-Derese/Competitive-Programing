a, b = [int(x) for x in input().split()]

count = 0
digits = 0

while digits < a:
    digits += len(str(b))
    count += 1
    b += 1

if (digits == a):
    print(count)

else:
    print(-1)
