from functools import cache

n = int(input())
nums = [int(i) for i in input().split()]
sortedNums = sorted(nums)
prefixSumA = [0]*(n+1)
prefixSumB = [0]*(n+1)

for i in range(1,n+2):
    try:
        prefixSumA[i] = prefixSumA[i-1] + nums[i-1]
        prefixSumB[i] = prefixSumB[i-1] + sortedNums[i-1]
    except:
        pass

@cache
def summation(t,l,r):
    if t==2:
        # print(prefixSumB[r], prefixSumB[l])
        return prefixSumB[r] - prefixSumB[l-1]
    else:
        # print(prefixSumA[r], prefixSumA[l])
        return prefixSumA[r] - prefixSumA[l-1]


for i in range(int(input())):
    t, l, r = [int(i) for i in input().split()]

    print(summation(t,l,r))

