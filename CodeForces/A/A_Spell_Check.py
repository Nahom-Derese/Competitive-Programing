for i in range(int(input())):
    a = int(input())
    timur = {"T","i","m","u","r"}
    b = input()
    x = set()
    for i in b:
        x.add(i)
    count = 0

    for i in x:
        if i in timur:
            count+=1
    
    if count==5 and len(b)==5:
        print("YES")
    else:
        print("NO")