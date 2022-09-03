from math import ceil

a = int(input())
prime_fact = []

def primeFactorization(c):
    for i in range(2,int(c**0.5)+1):
        if(c%i == 0):
            prime_fact.append(i)
            primeFactorization(c/i)
            return

primeFactorization(a)
b=1
for i in prime_fact:
    b*=i
prime_fact.append(int(a/b))

print(prime_fact)