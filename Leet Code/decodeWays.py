class Solution:
    def numDecodings(self, s: str) -> int:
        g = [e for e in s]
        ways = {}
        e = []
        for i in range(1,27):
            ways[chr(i+64)] = i
        if g[0] == "0":
            return 0
        else:
            for i in range(len(g)):
                if i <= len(g)-1 and int(g[i]) == 0:
                    g[i-1] = 'X'
                    g.pop(i)
                    
            for i in range(len(g)):
                if g[i] != 'X' and int(g[i]) == 1:
                    if i < len(g)-1 and g[i+1] != 'X':
                        e.append(i)

                if g[i] != 'X' and int(g[i]) == 2:
                    if i < len(g)-1 and int(g[i+1]) < 7:
                        e.append(i)
        t = []
        ans = 1
        if len(e) >= 2:
            for i in range(len(e)-1):
                if i < len(e)-1 and e[i] == e[i+1] - 1:
                    e.pop(i+1)
                    t.append(3)
                else:
                    t.append(1)
            for i in t:
                ans *= i
            return ans
        else:
            return 2
        
# print(Solution.numDecodings(Solution, '2222'))