
keyboard = [['q','w','e','r','t','y','u','i','o','p'],
            ['a','s','d','f','g','h','j','k','l'],
            ['z','x','c','v','b','n','m']]

a = input()
answer = []
for i in range(int(a)):
    b,c = input().split()
    d = int(c)
    list = []
    for j in range(d):
        e = input()
        n = 0
        for k in range(len(b)):
            if b[k] == e[k]:
                continue
            else:
                pair = []
                for r in range(len(keyboard)):
                    for w in range(len(keyboard[r])):
                        if b[k] == keyboard[r][w] or e[k] == keyboard[r][w]:
                            pair.append([r,w])
                        elif len(pair) == 2:
                            break
                ans = abs((pair[0][0] - pair[1][0])) + abs((pair[0][1] - pair[1][1]))
                n += ans
        list.append("{} {}".format(e,n))
    answer.append(list)

for a in answer:
    a.sort(key=(lambda x: (int(x.split()[1]), x.split()[0])))
    for b in a:
        print(b)

        