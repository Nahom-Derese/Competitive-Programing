for i in range(int(input())):
    n, x = map(int, input().split())
    nums = sorted(list(map(int, input().split())))

    for i in range(n):
        if nums[n+i] - nums[i] < x:
            print("NO")
            break
    else:
        print("YES")
