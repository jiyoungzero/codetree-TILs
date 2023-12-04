# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
edges = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
dist = [
    [0] * (n + 1)
    for _ in range(n + 1)
]

# n - 1개의 간선 정보를 입력받습니다.
for _ in range(n - 1):
    x, y, d = tuple(map(int, input().split()))

    # 간선 정보를 인접리스트에 넣어줍니다.
    edges[x].append((y, d))
    edges[y].append((x, d))


# DFS를 통해 st로부터 모든 정점까지의 거리를 탐색합니다.
def dfs(st, x):
    for y, d in edges[x]:
        # 이미 방문한 노드는 스킵합니다.
        if visited[y]: 
            continue
        
        visited[y] = True

        # st로부터의 거리를 갱신합니다.
        dist[st][y] = dist[st][x] + d
        dfs(st, y)


# 각 n개의 정점에 대해, 모든 노드간의 거리를 DFS로 갱신해줍니다.
for i in range(1, n + 1):
    for j in range(1, n + 1): 
        visited[j] = False
    
    visited[i] = True
    dfs(i, i) # start, now_node

# m개의 노드 쌍을 입력받고, 두 노드 쌍 간의 거리를 바로 출력해줍니다.
for _ in range(m):
    x, y = tuple(map(int, input().split()))
    print(dist[x][y])