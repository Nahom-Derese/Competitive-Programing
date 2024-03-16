for i in range(int(input())):

    n, new = [int(i) for i in input().split()]

    num = list(input())
    
    pos = n
    for i in range(n):
        if new > int(num[i]):
            pos = i
            break
    
    num.insert(pos, str(new))

    print("".join(num))
