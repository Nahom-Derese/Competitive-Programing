def solve():
    n = int(input())
    nums = [int(i) for i in input().split()]
    

    prefix_XOR=[nums[0]]
    for i in range(1,n):
        prefix_XOR.append(prefix_XOR[-1]^nums[i])

    # already if all are equal
    if prefix_XOR[-1]==0:
        return "YES"

    for i in range(n):
        first=prefix_XOR[i]
        for j in range(i+1,n):
            second=prefix_XOR[j]^first
            third=prefix_XOR[-1]^prefix_XOR[j]
            if first==second==third:
                return "YES"

    return "NO"

for _ in range(int(input())):
    print(solve())
