# Problem: Fraction Addition and Subtraction - https://leetcode.com/problems/fraction-addition-and-subtraction/

class Solution:

    def simplify(self, numerator, denominator):
        if (numerator == 0):
            return "0/1"
        if (denominator == 0):
            return "undefined"
    
        GCD = gcd(numerator, denominator)
        numerator = numerator // GCD
        denominator = denominator // GCD
    
        return f"{numerator}/{denominator}"
    
    def calc(self, fractions):
        num, denum = list(zip(*fractions))

        y = lcm(*denum)
        x = 0
        for i in range(len(fractions)):
            x+=num[i] * (y // denum[i])
        
        return self.simplify(x, y)

    def fractionAddition(self, expression: str) -> str:
        fractions = re.findall("[\+\-]*\d+/\d+", expression)
        fractions = [list(map(int, fraction.split("/"))) for fraction in fractions]
        
        return self.calc(fractions)

            
