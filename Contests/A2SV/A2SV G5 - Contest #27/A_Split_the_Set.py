def solve():
    n  = int(input())
    nums = list(map(int, input().split()))

    odd_counts = even_counts =  0

    for num in nums:
        odd_counts += num & 1
        even_counts += not(num & 1)

    # print(odd_counts, even_counts)

    return odd_counts == even_counts

for _ in range(int(input())):
    if solve():
        print("Yes")
    else:
        print("No")
