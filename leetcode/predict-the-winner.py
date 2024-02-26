class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
       
        N = len(nums)

        @cache
        def dp(left, right):
            if left > right:
                return 0

            choose_left = nums[left] - dp(left+1, right)
            choose_right = nums[right] - dp(left, right-1)
            
            return max(choose_left, choose_right)

        return dp(0, N-1) >= 0