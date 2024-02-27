def gcd(a, b):
    if not a % b:
        return b
    return gcd(b, a % b)


print(gcd(24, 22))