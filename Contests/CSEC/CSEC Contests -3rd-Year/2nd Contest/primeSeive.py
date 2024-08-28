a = [int(i) for i in input().split()]

b = range(a[0])

for i in range(a[1]):
    c = input()


def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(a**0.5)+1):
        if a % i == 0:
            return False
            break
        elif i == int(a**0.5):
            return True
