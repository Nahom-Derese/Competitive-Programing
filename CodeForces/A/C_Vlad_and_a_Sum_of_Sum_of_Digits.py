listt = []
def ans(n):
    ans = 0
    for i in range(1,n+1):
        ans+=sum([int(j) for j in str(i)])
    return ans

# for i in range(200000+1):
#     listt.append(ans(i))


for i in range(int(input())):
    x = int(input())
    print(ans(x))
