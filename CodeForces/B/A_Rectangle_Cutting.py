for i in range(int(input())):
    x, y= map(int, input().split())

    if x % 2 == 1 and y % 2 == 1:
        print("No")
    elif x % 2 == 0 and y % 2 == 0:
        u = max(x, y)
        if u/2 == min(x, y):
            u = min(x, y)
            if u/2 == max(x, y):
                print("No")
            else:
                print("Yes")
        else:
            print("Yes")
    elif x % 2 == 1 and y % 2 == 0:
        if y/2 == x:
            print("No")
        else:
            print("Yes")
    else:
        if x/2 == y:
            print("No")
        else:
            print("Yes")
