n, m = [int(i) for i in input().split()]

pages = [int(i) for i in input().split()]

dict = {}
set = {}

for i in range(m):
    a, b = [int(i) for i in input().split()]
    dict[b-1] = a-1
    if (a-1 in set.keys()):
        set[a-1].append(b-1)
    else:
        set[a-1] = [b-1]

Culminating = [a for a in range(n) if a not in set.keys()]

for i in range(1,len(pages)):
    if (i in dict.keys()):
        pages[i] += pages[dict[i]]
    
possibleAns = float('inf')

for i in set.keys():
    if (len(set[i]) > 1):
        page = [pages[k] for k in set[i] if k in Culminating]
        page.sort()
        if (len(page) > 1 and possibleAns > page[0] + page[1] - pages[i]):
            possibleAns = (page[0] + page[1] - pages[i]) 

if (possibleAns == float('inf')):
    y = [pages[i] for i in Culminating]
    y.sort()
    possibleAns = y[0] + y[1]

print(possibleAns)