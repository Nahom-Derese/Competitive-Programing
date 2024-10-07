
def solve(target):
    cache = {}
        
    def dp(summ):

        if summ > target:
            return float("inf")
        
        if summ == target:
            return 0

        if summ in cache:
            return cache[summ]
        
        if target - summ < 3:
            return target - summ

        
        cache[summ] = min(dp(summ+5), dp(summ+3))
        return cache[summ]
    
    print(dp(0))
    

for _ in range(int(input())):
    n = int(input())
    solve(n)
