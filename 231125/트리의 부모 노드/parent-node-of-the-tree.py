import sys
input = sys.stdin.readline


n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(n+1)
parent = [0]*(n+1)
def dfs(x):
    for leaf in graph[x]:
        if not visited[leaf]:
            parent[leaf] = x
            visited[leaf] = True
            dfs(leaf)
dfs(1)
for i in range(2, n+1):
    print(parent[i])