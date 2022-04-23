x = int(input())

Answer = []

for i in range(x):
    Ans = []
    nodes,edges,queries = input().split()
    nodes = int(nodes)
    edges = int(edges)
    queries = int(queries)
    graph = [input().split() for i in range(nodes)]
    ques = [input().split() for i in range(queries)]
    for j in range(nodes):
        for k in range(nodes):
            graph[j][k] = int(graph[j][k])
    for q in range(queries):
        for y in range(2):
            ques[q][y] = int(ques[q][y])
    for u in ques:
        if graph[u[0]][u[1]] == 1:
            Ans.append(1)
        else:
            if graph[u[0]] == [0 for e in range(nodes)]:
                Ans.append(0)
            for r in range(nodes):
                if graph[u[0]][r] == 1:
                    if graph[r][u[2]] == 1:
                        Ans.append(1) 
    Answer.append(Ans)

for p in range(len(Answer)):
    print("Case {0}".format(p+1))
    for w in Answer[p]:
        print(w)