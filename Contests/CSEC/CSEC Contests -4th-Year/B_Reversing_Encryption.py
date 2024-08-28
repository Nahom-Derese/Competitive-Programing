n = int(input())
a = list(input())

for i in range(1, n+1):
    if not n%i:
        a = a[:i][::-1] + a[i:]

print("".join(a))