class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        ans = [-1,-1]

        def findLR(left=True):
            l = 0
            r = len(nums) - 1
            nonlocal ans
            while l <= r:
                middle = l + (r-l) // 2

                if nums[middle] < target:
                    l = middle + 1
                elif nums[middle] > target:
                    r = middle - 1
                elif left:
                    if middle == 0 or nums[middle-1] != target:
                        ans[0] = middle
                        break
                    else:
                        r = middle - 1
                else:
                    if middle == len(nums)-1 or nums[middle+1] != target:
                        ans[1] = middle
                        break
                    else:
                        l = middle + 1

        findLR()
        findLR(False)

        return ans 