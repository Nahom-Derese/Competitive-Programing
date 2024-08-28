from heapq import *
test = int(input())
for _ in range(test):
    ln = int(input())
    s = input()
    heap = []
    for i in range(ln):
        heappush(heap,(-ord(s[i]),i))
    charr = []
    cur_ind = -1
    while heap:
        cur = heappop(heap)
        if charr and chr(-cur[0])==charr[-1]:
            charr.append(chr(-cur[0]))
            cur_ind = max(cur_ind, cur[1])
        if cur[1]>cur_ind:
            charr.append(chr(-cur[0]))
            cur_ind = cur[1]
    ptr = len(charr)-1
    ptr_f = 0
    ans = list(s)
    for i in range(ln):
        if ptr_f<len(charr) and ans[i] == charr[ptr_f]:
            ans[i]=charr[ptr]
            ptr-=1
            ptr_f+=1
    if ans != sorted(s):
        print(-1)
    else:
        v = len(charr) 
        res = v - charr.count(charr[0]) 
        print(res)


