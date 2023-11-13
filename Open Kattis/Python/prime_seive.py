def primesieve(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    primes = []
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False

    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)

    return primes

# Read input value
n = int(input())

# Generate primes and count
prime_list = primesieve(n)
prime_count = len(prime_list)

# Print the count and list of prime numbers
print(prime_count)
for prime in prime_list:
    print(prime)
