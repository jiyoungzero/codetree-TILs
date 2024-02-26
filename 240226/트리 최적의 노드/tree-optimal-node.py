import sys
input = sys.stdin.readline 
sys.setrecursionlimit(100000)



n = int(input())
farthest_dist =  [[] for _ in range(n+1)]
edges = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    edges[a].append((b, 1))
    edges[b].append((a, 1))

visited = [False]*(n+1)
distance = [0]*(n+1)

def dfs(node, total):
    for leaf, dist in edges[node]:
        if not visited[leaf]:
            visited[leaf] = True
            distance[leaf] = total + dist
            dfs(leaf, distance[leaf])
    

def find_farthest_dist(x):
    for i in range(1, n+1):
        visited[i] = False
        distance[i] = 0
    
    visited[x] = True
    dfs(x, 0)

    return max(distance), distance.index(max(distance))

_, farthest_node = find_farthest_dist(1)
answer, _ = find_farthest_dist(farthest_node)
print((answer+1) // 2)