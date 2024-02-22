class Solution:
    def smallestNumber(self, num: int) -> int:
        if not num:
            return 0
        if num < 0:
            x = sorted(str(num)[1:], reverse=True)
            ans = "".join(x)
            return int(f"-{ans}")
        x = sorted(str(num))
        i = 0
        while x[i] == '0':
            i+=1
        if i == 0:
            return int("".join(x))
        x[i], x[0] = x[0], x[i]
        return int("".join(x))