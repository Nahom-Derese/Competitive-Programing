class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        running_sum = 0
        prev_sums = defaultdict(int)

        prev_sums[0] = 1

        ans = 0
        for i in nums:
            running_sum += (i%2)
            ans+=prev_sums[running_sum-k]
            prev_sums[running_sum]+=1

        return ans