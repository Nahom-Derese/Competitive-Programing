inp = int(input())

a = [input() for i in range(inp)]

ans=[]

for i in a:
    count = 0
    for j in range(len(i)):
        if i[j] == "U":
            count += 1
            if j==len(i)-1:
                ans.append(count)
        else:
            ans.append(count)
            break
for i in ans:
    print(i)
