n = int(input())

def summation(n):
    ans = int((n/2)*(n+1))
    return ans

def answer(x):
    global n
    for i in range(1,x):
        print(i, end=' ')
    print(n-summation(x))

for i in range(1,n):
    if n - summation(i) < i:
        print(i)
        answer(i)
        break
    