class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        my_dict={'(':')','{':'}','[':']'}
        for i in s:
            if stack and (stack[-1] in my_dict) and (i==my_dict[stack[-1]]):
                stack.pop()
            else:
                stack.append(i)
        
        return stack == []