from bisect import bisect_left

n, m = [int(i) for i in input().split()]

songs = [0]

for _ in range(n):
    ci, ti = [int(i) for i in input().split()]
    songs.append(songs[-1] + (ci * ti))

moments = [int(i) for i in input().split()]
# print(songs)
for moment in moments:
    print(bisect_left(songs, moment))
    