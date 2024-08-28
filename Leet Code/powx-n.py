
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1.00000
        if n == 1:
            return x
        elif n < 0:
            if n%2==0:
                return self.myPow(x, n/2) ** 2
            return (1/x) * self.myPow(x, n+1)
        elif n > 0 :
            if n%2==0:
                return self.myPow(x, n/2) ** 2
            print("{} is odd".format(n))
            return x * self.myPow(x, n-1)