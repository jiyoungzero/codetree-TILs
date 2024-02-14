import sys
input = sys.stdin.readline 
sys.setrecursionlimit(100000)
n = int(input())
edges = [[] for _ in range(n+1)]
visited = [False]*(n+1)
distance = [0]*(n+1)

for _ in range(n-1):
    a, b, d = map(int, input().split())
    edges[a].append((b, d))
    edges[b].append((a, d))

def dfs(node, total):
    for leaf, d in edges[node]:
        if not visited[leaf]:
            visited[leaf] = True
            distance[leaf] = total + d
            dfs(leaf, total+d)

def find_far_vertex(x):
    # visited = [False]*(n+1)
    # distance = [0]*(n+1)
    for i in range(1, n + 1):
        visited[i] = False
        distance[i] = 0
    visited[x] = True
    dfs(x, 0)

    return distance.index(max(distance)), max(distance)

nxt_vertex, _ = find_far_vertex(1)
_, answer = find_far_vertex(nxt_vertex)

print(answer)