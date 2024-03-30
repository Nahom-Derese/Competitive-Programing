import sys
from collections import *
from itertools import *
from math import *

def prime_sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return set([i for i in range(2, n + 1) if is_prime[i]])

def is_perfect_square(n):
    sq = sqrt(n)
    return (int(sq) == sq, sq)

primes = prime_sieve(10**6)

n = int(sys.stdin.readline().strip())

for num in  [int(i) for i in sys.stdin.readline().split()]:
    p_s = is_perfect_square(num)
    if p_s[0] and p_s[1] in primes:
        print("YES")
    else:
        print("NO")