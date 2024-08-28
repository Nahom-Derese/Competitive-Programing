# Problem: C - Palindromic Sum Representations - https://codeforces.com/gym/524965/problem/C

import sys 

def lsinp():
    return sys.stdin.readline().strip().split()
def liinp():
    return list(map(int, sys.stdin.readline().strip().split()))
def sinp():
    return sys.stdin.readline().strip()
def iinp():
    return int(sys.stdin.readline().strip())
    
palindromes=[]
for i in range(1,40001):
    var=str(i)
    if var==var[::-1]:
        palindromes.append(i)
t = iinp()
mod=10**9+7

dp=[0]* 40001
dp[0]=1
for num in palindromes:
    for j in range(num, 40001):
        dp[j]+=dp[j-num]
        dp[j]%=mod

for _ in range(t):
    n=iinp()
    print(dp[n])
