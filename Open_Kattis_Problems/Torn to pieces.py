def dfs(adjList, s, e):
    stack = []
    passed = {i:False for i in adjList.keys()}
    stack.append(s)
    output = []
    while stack:
        temp = stack.pop()
        if(temp[:11] == "TraceBack :"):
            if len(output) > 1:
                output = output[:len(output) - 1 - output[::-1].index(temp[12:])]
            continue
        output.append(temp)
        if(temp == e):
            return output
        for i in adjList[temp]:
            if len(adjList[temp]) > 1:
                if not passed[i]:
                    stack.append('TraceBack : ' + i)
                    stack.append(i)
                    passed[i] = True
            if not passed[i]:
                stack.append(i)
                passed[i] = True
    return []

a = int(input())
adjList = {}

for i in range(a):
    u = input().split()
    adjList[u[0]] = {i for i in u[1:]}
    for i in u[1:]:
        if(adjList.get(i)):
            adjList[i].add(u[0])
        else:
            adjList[i] = {u[0]}


s,e = input().split()

answer = dfs(adjList, s, e)

if not answer:
    print("no route found", end="")

for i in answer:
    print(i , end=" ")
print()