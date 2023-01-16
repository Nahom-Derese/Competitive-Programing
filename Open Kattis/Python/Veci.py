a = input()

def swap(a : str,b,c):
    return a[:b] + a[c] + a[b+1:c] + a[b] + a[c+1:]

ans = '0'

for i in range(len(a)-2,-1,-1):
    if a[i] < a[i+1]:
        ans = swap(a,i,i+1)
        sort = list(ans[i+1:])
        sort.sort()
        ans = "".join(list(ans[:i+1])+sort)
        break

print(ans)

    
