shows = []
for i in range(int(input())):
    shows.append(tuple([int(i) for i in input().split()]))

shows.sort()

TV1 = [(-1,-1)]
TV2 = [(-1,-1)]

for l,r in shows:        
    if l > TV1[-1][1]:
        TV1.append((l,r))
    elif l > TV2[-1][1]:
        TV2.append((l,r))
    else:
        print("NO")
        break
else:
    print("YES")