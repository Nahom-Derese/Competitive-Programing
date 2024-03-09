from bisect import *

n, q = map(int, input().split())
nums = list(map(int, input().split()))

anomalies = []

def validate(array):
    global anomalies
    for i in range(2, len(array)):
        if array[i-2] >= array[i-1] and array[i-1] >= array[i]:
            anomalies.append(i)
            # return False
    return True

for _ in range(q):
    l, r = map(int, input().split())
    my_range = r - l + 1
    start = bisect_right(anomalies, l)
    end = bisect_right(anomalies, r)

    anomalies_in_range = end - start
    print(l, r , start, end)