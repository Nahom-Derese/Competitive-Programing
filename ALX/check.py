class Solution:
    def canSortArray(self, nums):
        binSet = {}
        for i in nums:
            binSet[i] = sum(map(int, list(bin(i).split('b')[-1])))
        
        sortednums = sorted(nums)
        
        x = 0
        for i in range(len(sortednums)):
            ogIndex = nums.index(sortednums[i])
            count = 0
            if i < ogIndex:
                for j in range(i, ogIndex):
                    if binSet[nums[j]] == binSet[nums[i]]:
                        count+=1
            else:
                for j in range(ogIndex, i):
                    if binSet[nums[j]] == binSet[nums[i]]:
                        count+=1
            
            if count == abs(ogIndex-i):
                x+=1
        return x == len(nums)
            


print(Solution.canSortArray(Solution, [75,34,30]))
print(Solution.canSortArray(Solution, [8,4,2,30,15]))
print(Solution.canSortArray(Solution, [1,2,3,4,5]))
print(Solution.canSortArray(Solution, [3,16,8,4,2]))