def solve():
    a,b = [int(i) for i in input().split()]
    return (a ^ b)
    

for _ in range(int(input())):
    print(solve())
