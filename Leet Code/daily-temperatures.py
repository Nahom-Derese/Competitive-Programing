class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = defaultdict(int)
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                x = stack.pop()
                ans[x] = i - x[1]
            stack.append((temperatures[i], i))
        
        return [ans[(temp, i)]  for i, temp in enumerate(temperatures)]
