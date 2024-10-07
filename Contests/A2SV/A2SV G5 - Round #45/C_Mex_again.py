n = int(input())
nums = list(map(int, input().split()))

nums.sort()

ans = 1

itr = 0

while itr < n:
    num = nums[itr]
    itr+=1
    ans+= int(ans <= num)

print(ans)