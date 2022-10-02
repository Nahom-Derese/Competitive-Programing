class Solution:
    def reverse(self, x: int) -> int:
        if x < 0 and x > -2**31:
            y = str(x)[1:][::-1]
            ans = int(y) * -1
            if ans > -2**31:
                return ans
            else:
                return 0
        elif x > 0 and x < 2**31 - 1:
            y = str(x)[::-1]
            ans = int(y)
            if ans < 2**31 - 1:
                return ans
            else:
                return 0
        else:
            return 0

print(Solution.reverse(Solution, 1534236469))