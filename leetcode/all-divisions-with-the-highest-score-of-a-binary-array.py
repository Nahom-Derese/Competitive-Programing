class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        count_ones = list(accumulate([0] + nums[::-1]))[::-1]
        count_zeros = [0] + list(accumulate([int(not(bool(i))) for i in nums])) 
        
        _max = -1
        ans = []
        for i in range(len(nums)+1):
            score = count_ones[i] + count_zeros[i]
            if score < _max:
                continue
            if score > _max:
                _max = score
                ans= []
            ans.append(i)

        return ans
