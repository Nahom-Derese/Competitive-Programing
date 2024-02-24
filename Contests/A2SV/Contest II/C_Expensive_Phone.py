for i in range(int(input())):
    n = int(input())

    prices = [int(i) for i in input().split()]

    monotonic = [0]

    ans = 0
   
    for i in prices:
        while monotonic and monotonic[-1] > i:
            monotonic.pop()
            ans+=1
        monotonic.append(i)
        
    print(ans)