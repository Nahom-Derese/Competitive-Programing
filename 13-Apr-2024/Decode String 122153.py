# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        

        def rec(string):
            i = 0
            res = ""
            while i < len(string):
                mul = ""
                while string[i].isdigit():
                    mul+=string[i]
                    i+=1
                
                if len(mul):
                    mul = int(mul)
                    stack = ["["]
                    s = i+2
                    i = s
                    while stack and i < len(string):
                        if string[i] == "]" and stack[-1] == "[":
                            stack.pop()
                        elif string[i] == "[":
                            stack.append(string[i])
                        i+=1
                    res += mul * rec(string[s-1:i-1])
                    continue
                else:
                    res += string[i]
                i+=1
            
            return res

        return rec(s)
            