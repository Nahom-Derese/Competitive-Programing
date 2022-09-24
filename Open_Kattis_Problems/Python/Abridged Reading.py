n, m = [int(i) for i in input().split()]

pages = [int(i) for i in input().split()]

dict = {i:[] for i in range(n)}
set = {}
arr = [-1 for i in range(n)]

for i in range(m):
    a, b = [int(i) for i in input().split()]
    arr[b-1] = a-1
    set[a-1] = []

for i in range(n):
    x = arr[i]
    while x != -1:
        dict[i].append(x)
        x = arr[x]

for i in set.keys():
    for j in range(m):
        if (i in dict[j]):
            set[i].append(j)
    



Culminating = [a for a in range(n) if a not in set.keys()]

for i in range(1,len(pages)):
    if (i in dict.keys() and len(dict[i]) > 0):
        pages[i] += pages[dict[i][0]]
    
sorted = sorted([pages[i] for i in dict.keys() if i in Culminating])
possibleAns = sorted[0] + sorted[1]

for i in set.keys():
    if (len(set[i]) > 1):
        page = [pages[k] for k in set[i] if k in Culminating]
        page.sort()
        if (len(page) > 1 and possibleAns > page[0] + page[1] - pages[i]):
            possibleAns = (page[0] + page[1] - pages[i]) 

print(possibleAns)