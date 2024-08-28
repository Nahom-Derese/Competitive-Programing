def solve():
    a, b, c, n = [int(i) for i in input().split()]
    
    high = max(a, b, c)
    minimum_needed = (high - a) + (high - b) + (high - c)
    # print(minimum_needed)
    if n < minimum_needed:
        return False
    
    if n == minimum_needed:
        return True


    return (n - minimum_needed) % 3 == 0

for _ in range(int(input())):
    if solve():
        print("YES")
    else:
        print("NO")
