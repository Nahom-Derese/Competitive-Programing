from math import inf

someArray = [4,8,9,3,6,8,12,4,2,8,5,3,10,1,7]

def dynamicSlidingWindows(a: list, n: int):
    minWindow = inf
    currentSum = 0
    currentWindowSize = 0
    count = 0
    for i in a:
        currentWindowSize += 1
        currentSum += i
            
        if currentSum >= n:
            if currentWindowSize == 1:
                return 1
            else:
                while currentSum - a[count - currentWindowSize + 1] >= n:
                        currentSum -= a[count - currentWindowSize + 1]
                        currentWindowSize -= 1
                minWindow = min(currentWindowSize, minWindow)
                    
        count += 1
    return minWindow

print(dynamicSlidingWindows(someArray, 38))