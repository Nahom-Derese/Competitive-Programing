wantToRead = int(input())

days = list(map(int,input().split()))

readedPages = 0
k = 0
while readedPages < wantToRead:
    i=days[k%7]
    readedPages+=i
    # print(k)
    if readedPages >= wantToRead:
        print(k%7+1)
    k += 1
