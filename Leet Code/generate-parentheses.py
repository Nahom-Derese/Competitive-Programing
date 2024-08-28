class Solution:
    def validateParenthesis(self, s: str) -> bool:
        stack = []

        for i in s:
            if not stack:
                stack.append(i)
            elif stack and stack[-1] == '(':
                if i == ')':
                    stack.pop()
                else:
                    stack.append('(')
            else:
                return False

        return not stack
    
    def validatePossiblity(self, s: str) -> bool:
        stack = []

        for i in s:
            if not stack:
                stack.append(i)
            elif stack and stack[-1] == '(':
                if i == ')':
                    stack.pop()
                else:
                    stack.append('(')
            else:
                return False

        return True

    def generateParenthesis(self, n: int) -> List[str]:

        ans = []

        def backtrack(current):
            # print(current)
            if len(current) == n*2:
                if self.validateParenthesis(current):
                    ans.append("".join(current))
                return 
                
            for i in ["(",")"]:
                val = "".join(current+[i])
                if val.count('(') <= n and self.validatePossiblity(val):
                    current.append(i)
                    backtrack(current)
                    current.pop()
            
        backtrack([])
        

        return ans