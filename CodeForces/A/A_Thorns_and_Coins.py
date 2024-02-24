for i in range(int(input())):
    n = int(input())
    inputt = input()
    coins = inputt.count('@')
    c = n
    for i in range(n-1):
        if inputt[i] == inputt[i+1] == '*':
            c = i
            break
    x = inputt[c:].count('@')
    print(coins-x)