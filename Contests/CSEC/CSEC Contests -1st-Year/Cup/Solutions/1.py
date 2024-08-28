g = {
    'a' : ['b', 'f'],
    'c' : ['r'],
    'r' : ['f','c'],
    'b' : ['a',],
    'f' : []
}

visited = set()

def dfs(visited, g , n):
    if n not in visited:
        print(n)
        visited.add(n)
        for neg in g[n]:
            dfs(visited, g, neg)

dfs(visited, g, 'a')
