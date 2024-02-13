import sys
sys.setrecursionlimit(100000)

# 변수 선언 및 입력:
n = int(input())
edges =[[] for _ in range(n + 1)]
visited = [False] * (n + 1)
dist = [0] * (n + 1)

# n - 1개의 간선 정보를 입력받습니다.
for _ in range(n - 1):
    x, y, d = tuple(map(int, input().split()))
    # 간선 정보를 인접리스트에 넣어줍니다.
    edges[x].append((y, d))
    edges[y].append((x, d))


# DFS를 통해 연결된 모든 정점을 순회합니다.
# 동시에 시작점으로부터의 거리를 같이 계산해줍니다.
def dfs(x, total_dist):
    # 노드 x에 연결된 간선을 살펴봅니다.
    for y, d in edges[x]:
        # 아직 방문해본적이 없는 노드인 경우에만 진행합니다.
        if not visited[y]:
            visited[y] = True
            dist[y] = total_dist + d
            dfs(y, total_dist + d)


# 정점 x로부터 가장 멀리 있는 정점 정보를 찾아줍니다.
def find_largest_vertex(x):
    # visited, dist 값을 초기화해줍니다.
    for i in range(1, n + 1):
        visited[i] = False
        dist[i] = 0
    
    # 정점 x를 시작으로 하는 DFS를 진행합니다.
    visited[x] = True
    dist[x] = 0
    dfs(x, 0)
    
    # 정점 x로부터 가장 멀리 떨어진 정점 정보를 찾습니다.
    farthest_dist = -1
    farthest_vertex = -1
    for i in range(1, n + 1):
        if dist[i] > farthest_dist:
            farthest_dist = dist[i]
            farthest_vertex = i

    # 가장 멀리 떨어진 정점 번호와 그때의 거리를 반환합니다.
    return farthest_vertex, farthest_dist


# 1번 정점으로부터 가장 멀리 있는 정점 정보를 찾습니다.
f_vertex, _ = find_largest_vertex(1)

# farthest vertex로부터 가장 멀리 있는 정점 정보를 찾습니다.
# 이때의 거리가 지름이 됩니다.
_, diameter = find_largest_vertex(f_vertex)

print(diameter)