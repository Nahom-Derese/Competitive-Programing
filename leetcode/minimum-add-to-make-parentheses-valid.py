class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = [s[0]]

        for i in s[1:]:
            if len(stack)>0 and stack[-1] == '(' and i == ')':
                stack.pop()
            else:
                stack.append(i)
        
        return len(stack)