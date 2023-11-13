def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Read input values
a, b = map(int, input().split())

# Calculate the GCD of a and b
result = gcd(a, b)

# Print the GCD
print(result)
