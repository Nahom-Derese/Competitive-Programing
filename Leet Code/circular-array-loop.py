class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        mapp = defaultdict(int)
        _len = len(nums)
        
        for i in range(_len):
            u = (i+nums[i]) % _len 
            if u == i:
                continue
            if nums[u] > 0 and nums[i] > 0:
                mapp[i] = u
            elif nums[u] < 0 and nums[i] < 0:
                mapp[i] = u

        visited = set()
        
        for i in mapp:
            itr = i
            target=i
            j=0
            while mapp[itr] in mapp and j<len(nums):
                # visited.add(itr)
                itr=mapp[itr]
                j+=1
                if target==itr:
                    return True
            
        return False 
        