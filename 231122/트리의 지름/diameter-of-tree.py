import sys
sys.setrecursionlimit(100000)

n = int(input())
edges = [[] for _ in range(n+1)]
visited = [False]*(n+1)
dist = [0]*(n+1)

# n-1개의 간선정보받기
for _ in range(n-1):
    x, y,d = tuple(map(int, input().split()))
    edges[x].append((y, d))
    edges[y].append((x, d))

# dfs를 통해 연결된 모든 정점을 순회합니다.
# 각 정점끼리의 거리 계산용 함수 
def dfs(parent, total_dist):
    for leaf, d in edges[parent]:
        if not visited[leaf]:
            visited[leaf] = True
            dist[leaf]= total_dist +d
            dfs(leaf,dist[leaf])

# x로부터 가장 멀리 있는 정점 y찾기
def find_farthest_node(x):
    # visited, dist초기화
    for i in range(1, n+1):
        visited[i] = False
        dist[i] = 0         

    visited[x] = True
    dist[x] = 0
    dfs(x, 0) # 정점x로부터의 모든 정점들의 거리 계산 

    farthest_dist = -1
    farthest_vertex = - 1
    for i in range(1, n+1):
        if dist[i] > farthest_dist:
            farthest_dist = dist[i]
            farthest_vertex = i

    return farthest_vertex, farthest_dist # x로부터 가장 먼 정점, 그 때의 거리

f_v, _ = find_farthest_node(1)
_, f_d = find_farthest_node(f_v)
print(f_d)