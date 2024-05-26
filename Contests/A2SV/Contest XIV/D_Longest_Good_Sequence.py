import sys

def prime_seive(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

def prime_factors(n):
    factors = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)

    return factors  

n = int(input())
nums = [int(i) for i in  input().split()]
dp = [0] *(max(nums) + 1)

if n == 1 and nums[0] == 1:
    print(1)
    sys.exit()

for num in nums:
    divisors = prime_factors(num)
    dp[num] = 1
    for div in divisors:
        dp[num] = max(dp[num], dp[div] + 1)

    for div in divisors:
        dp[div] = max(dp[div], dp[num])
print(max(dp))