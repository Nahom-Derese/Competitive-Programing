class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        running_sum = 0
        prev_sums = defaultdict(int)

        prev_sums[0] = 1

        ans = 0
        for i in nums:
            running_sum+=i
            ans+=prev_sums[running_sum%k]
            prev_sums[running_sum%k]+=1

        return ans