a,b = list(map(int,input().split()))

MOD = 10**9+7

a%=MOD

b%=MOD

c=a+b

c%=MOD

print(c)