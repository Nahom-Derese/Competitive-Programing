class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort(reverse=True)
        
        ans = 0
        for i in range(len(processorTime)):
            ans = max(tasks[i*4 + 3] + processorTime[i], ans)

        return ans