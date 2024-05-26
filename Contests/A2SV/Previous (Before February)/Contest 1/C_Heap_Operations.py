from heapq import heappush, heappop

heap = []
ans = []


def solve(c, n):
    res = []
    while heap and n > heap[0]:
        res.append("removeMin")
        heappop(heap)

    if not heap or n != heap[0]:
        heappush(heap, n)
        res.append(f"insert {n}")

    res.append(f"{c} {n}")
    ans.extend(res)
    

for _ in range(int(input())):
    command = input()

    if command.__contains__(" "):
        c, n = command.split(" ")
        n = int(n)

        if c == "insert":
            ans.append(command)
            heappush(heap, n)
        else:
            solve(c, n)
    else:
        if heap:
            heappop(heap)
            ans.append(command)
        else:
            ans.append("insert 5")
            ans.append(command)

print(len(ans))
for i in ans:
    print(i)