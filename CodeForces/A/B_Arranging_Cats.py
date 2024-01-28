t = int(input())

for i in range(t):
    a = int(input())

    ans = 0

    binary1 = input()
    binary2 = input()

    count1 = sum([int(i) for i in binary1])
    count2 = sum([int(i) for i in binary2])

    # print(count1,count2)

    for k in range(a):
        if binary1[k] != binary2[k]:
            ans+=1

    ans-=count2
# 
    print(ans)
