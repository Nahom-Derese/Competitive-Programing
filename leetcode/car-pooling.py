class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pre_sum = [0] * 1010
        for a, b, c in trips:
            pre_sum[b] += a
            pre_sum[c] -= a

        pre_sum = accumulate(pre_sum)
        
        return max(pre_sum) <= capacity

        