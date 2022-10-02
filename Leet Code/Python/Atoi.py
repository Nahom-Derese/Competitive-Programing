class Solution:
    def myAtoi(self, s: str) -> int:
        w = s.strip()
        count = 0
        if count < len(w) and not (w[count].isnumeric() or (w[count] == '-' and count+1 < len(w) and w[count+1].isnumeric() or w[count] == '+' and count+1 < len(w) and w[count+1].isnumeric())):
            return 0
        start = count
        try:
            if w[count] == '-' or w[count] == '+':
                count += 1
            while w[count].isnumeric() and count < len(w):
                count += 1
        except:
            pass
        end = count
        ans = w[start:end]
        if ans == '':
            return 0
        if (int(ans) <= 0 and int(ans) > -2**31) or (int(ans) >= 0 and int(ans) < 2**31 - 1):
            return int(ans)
        else:
            if int(ans)>0:
                return 2147483647
            else:
                return -2147483648
        
# print(Solution.myAtoi(Solution, "00000-42a1234"))