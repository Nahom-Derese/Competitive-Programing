for i in range(int(input())):
    a = int(input())
    b = list(map(int, input().split()))

    l = 0
    r = 0
    running_postive_sum = b[0]
    window_sum = b[0]
    while r<a:
        if r == 0:
            r+=1
            continue
        if (b[r]%2 + b[r-1]%2) == 1:
            window_sum += b[r]
            if b[r] > 0:
                running_postive_sum+=b[r]
            
            if b[r] < 0 and (abs(b[r]) > running_postive_sum):
                window_sum=b[r]
                l = r
            r+=1

        else:
            r+=1
            l = r

       
    print(window_sum)