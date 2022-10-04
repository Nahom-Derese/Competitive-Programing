class Solution:
    def letterCombinations(self, digits: str):
        maps = {
            1: [],
            2: ['a','b','c'],
            3: ['d','e','f'],
            4: ['g','h','i'],
            5: ['j','k','l'],
            6: ['m','n','o'], 
            7: ['p','q','r','s'],
            8: ['t','u','v'],
            9: ['w','x','y','z'],
            }

        ans= []
            
        def back(i, string):
            if len(string) == len(digits):
                ans.append(string)
                return
            
            for char in maps[int(digits[i])]:
                back(i + 1, string + char)
        
        back(0,'')

        if ans[0] == '':
            return []
        return ans
        

# print (Solution.letterCombinations(Solution, ""))