# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_xor = [0]

        for num in arr:
            prefix_xor.append(prefix_xor[-1] ^ num)
        
        def xor_q(pair):
            l, r = pair
            return prefix_xor[r+1] ^ prefix_xor[l]
        
        return list(map(xor_q, queries))