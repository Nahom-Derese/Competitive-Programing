for i in range(int(input())):
    u = [x for x in input().split()]

    n = int(u[0])
    c = u[1]

    string = input()

    i = 0
    startingPos = -1
    first_g = -1
    ans = []

    if len(string)==1:
        print(0)
        continue

    if c == 'g':
        print(0)
        continue

    for g in range(len(string)):
        if string[g] == 'g':
            first_g = g+1
            break

    while i < (n + first_g):
        if startingPos != -1 and string[i%n] == 'g':
            ans.append(i - startingPos)
            startingPos = -1
        
        if  startingPos == -1 and  string[i%n] == c:
            startingPos = i

        i+=1

    print(max(ans))
            