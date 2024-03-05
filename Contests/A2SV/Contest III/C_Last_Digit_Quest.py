from collections import Counter

def backtrack(summ, freq, idx):
    if idx == 3:
        return summ % 10 == 3
            
    for i in freq.keys():
        if freq[i]:
            freq[i]-=1
            if backtrack(summ+i, freq, idx+1):
                return True
            freq[i]+=1

    return False


for i in range(int(input())):
    n = int(input())

    nums = [int(i[-1]) for i in input().split()]

    count = Counter(nums)

    for i in count:
        count[i] = min(3, count[i])

    print("YES") if backtrack(0, count, 0) else print("NO")