class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, ans = [], defaultdict(lambda x: -1)

        for i in nums2:
            while stack and stack[-1] < i:
                ans[stack[-1]] = i
                stack.pop()
            stack.append(i)
        for i in stack:
            ans[i] = -1

        return [ans[i] for i in nums1]