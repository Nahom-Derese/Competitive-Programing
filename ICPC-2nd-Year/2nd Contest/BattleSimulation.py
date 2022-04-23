k = int(input())
count = 0
i = 19
while count < k:
    digit = [int(x) for x in list(str(i))]
    if (sum(digit) == 10):
        count += 1
    i += 9

print(i-9)