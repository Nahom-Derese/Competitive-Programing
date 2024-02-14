class Solution:
    def intToRoman(self, num: int) -> str:
        x = {
                1: 'I',
                5: 'V',
                10: 'X',
                50: 'L',
                100: 'C',
                500: 'D',
                1000: 'M',
            }
        
        string = str(num)[::-1]
        numbers = []
        
        for i in range(len(string)-1, -1, -1):
            temp = str(string[i]) + "0" * i
            numbers.append(int(temp))
        
        ans = ""

        for i in numbers:
            first_digit = int(str(i)[0])
            half = "5" + "0" * (len(str(i)) - 1 )
            halfByOne = "1" + "0" * (len(str(i))-1 )
            if i in x:
                ans += x[i]
            elif first_digit == 4:
                ans += x[int(halfByOne)]
                ans += x[int(half)]
            elif first_digit == 9:
                half = "10" + "0" * (len(str(i)) - 1 )
                ans += x[int(halfByOne)]
                ans += x[int(half)]
            elif first_digit > 4:
                minus5 = first_digit - 5
                ans += x[int(half)]
                ans += x[int(halfByOne)] * (first_digit - 5)
            else:
                ans += x[int(halfByOne)] * first_digit

        return ans


Solution().intToRoman(58)