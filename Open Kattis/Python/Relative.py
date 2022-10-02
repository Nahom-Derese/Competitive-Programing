while True:
    try:
        a = int(input())
        prime_fact = {}
        possible = [i for i in range(1,a//2+1)]
        def primeFactorization(c):
            for i in range(2,int(c**0.5)+1):
                if(c%i == 0):
                    if i in prime_fact.keys():
                        prime_fact[i] += 1
                    else:
                        prime_fact[i] = 1
                    primeFactorization(c/i)
                    return

        primeFactorization(a)
        b=1
        for i in prime_fact.keys():
            b *= i ** prime_fact[i]

        if a/b in prime_fact.keys():
            prime_fact[a//b] += 1
        else:
            prime_fact[a//b] = 1

        if  len(prime_fact.keys())==1 and [i for i in prime_fact.keys()][0] == a:
            print(a-1)
            
        else:
            for i in prime_fact.keys():
                for j in possible:
                    if j%i == 0:
                        possible.remove(j)
            print(len(possible) * 2)
    except:
        break