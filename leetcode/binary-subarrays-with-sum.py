class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        m = defaultdict(int)
        m[0] = 1

        run_sum = itr = ans = 0

        for num in nums:
            run_sum += num
            
            if run_sum - goal in m:
                ans+=m[run_sum - goal]
            
            m[run_sum]+=1


        return ans