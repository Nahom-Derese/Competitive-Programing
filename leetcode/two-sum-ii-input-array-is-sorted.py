class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1

        while r > l:
            if numbers[r] + numbers[l] > target:
                r-=1 
            elif numbers[r] + numbers[l] < target:
                l+=1
            else:
                return [l+1,r+1]