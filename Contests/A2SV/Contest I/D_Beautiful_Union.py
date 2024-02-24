from collections import Counter

for i in range(int(input())):
    n = int(input())

    nums_1 = list(map(int, input().split()))
    nums_2 = list(map(int, input().split()))

    c_1= Counter()
    c_2= Counter()

    l = r = 0
    while r < n-1:
        while nums_1[l] == nums_1[r]:
            r+=1
        c_1[nums_1[l]] = max(c_1[nums_1[l]], r-l)
        l=r
    
    c_1[nums_1[l]] = max(c_1[nums_1[l]], r-l)

    l = r = 0
    while r < n-1:
        while nums_2[l] == nums_2[r]:
            r+=1
        c_2[nums_2[l]] = max(c_2[nums_2[l]], r-l)
        l=r
        
    c_2[nums_2[l]] = max(c_2[nums_2[l]], r-l)

    print(c_1)
    print(c_2)