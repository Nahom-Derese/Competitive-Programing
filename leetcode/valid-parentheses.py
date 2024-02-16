class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openn=['(','{','[']
        close=[')','}',']']
        for i in s:
            if len(stack)>0:
                for j in range(3):
                    if len(stack)>0 and (stack[-1] == openn[j]) and (i == close[j]):
                        stack.pop()
                        break
                else:
                    stack.append(i)
            else:
                stack.append(i)
        print(len(stack))
        return len(stack) == 0