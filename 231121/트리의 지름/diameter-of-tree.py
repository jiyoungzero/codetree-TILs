v = int(input())
graph = [[] for _ in range(v+1)]
visited = [False]*(v+1)
dist = [0]*(v+1)

for _ in range(v-1):
    a, b, edge = map(int, input().split())
    graph[a].append((b, edge))
    graph[b].append((a, edge))

def dfs(x, dist_from_start):
    for leaf, d in graph[x]:
        if not visited[leaf]:
            visited[leaf] = True
            dist[leaf] = dist_from_start + d
            dfs(leaf, dist[leaf])

def find_longest_dist(x):
    # 초기화
    for i in range(1, v+1):
        visited[i] = False
        dist[i] = 0
    

    # 정점 x에서 시작
    visited[x] = True
    dist[x] = 0
    dfs(x, 0)

    # 정점 x로 부터 가장 멀리 떨어진 정점 정보 찾기
    farthest_dist = -1
    farthest_node = -1
    for i in range(1, v+1):
        if dist[i] > farthest_dist:
            farthest_dist = dist[i]
            farthest_node = i
    return farthest_dist, farthest_node

_, f_node = find_longest_dist(1) # 1번 정점에서 가장 먼 정점 정보 겟
answer_dist, _ = find_longest_dist(f_node) # f_node에서 찾은 가장 먼 정점까지의 거리
print(answer_dist)