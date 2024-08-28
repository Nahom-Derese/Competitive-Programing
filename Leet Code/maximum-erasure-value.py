class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans = current = l = r = 0

        mapp = set()

        while r < len(nums):
            current += nums[r]

            while nums[r] in mapp:
                mapp.remove(nums[l])
                current -= nums[l]
                l+=1
            mapp.add(nums[r])

            ans = max(ans, current)

            r+=1

        return ans