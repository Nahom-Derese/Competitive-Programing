import math

def count_factors(n, p):
    count = 0
    while n % p == 0:
        count += 1
        n //= p
    return count

def has_factovisors(n, m):
    if m == 0:
        return n == 1
    if n <= m:
        return False

    for p in range(2, int(math.sqrt(m)) + 1):
        if m % p == 0:
            exp = count_factors(m, p)
            if exp > count_factors(n, p):
                return False
    if m > 1 and n <= m:
        return False
    return True

# Read input values
n, m = map(int, input().split())

# Check if n! divides m
if has_factovisors(n, m):
    print(f"{m} divides {n}!")
else:
    print(f"{m} does not divide {n}!")
