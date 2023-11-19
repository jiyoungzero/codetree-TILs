n = int(input())

edges = [[] for _ in range(n+1)]
visited = [False] * (n+1)
parent = [0] * (n+1)

# n-1개의 간선 정보
for _ in range(n-1):
    x, y  = tuple(map(int, input().split()))
    edges[x].append(y)
    edges[y].append(x)

# dfs방식의 트리 순회
# 진행되는 간선에 대해 (부모, 자식) 관계를 재정의
def travel(x):
    for y in edges[x]:
        if not visited[y]:
            visited[y] = True
            parent[y] = x

            travel(y)

visited[1] = True
travel(1)
for p in parent[2:]:
    print(p)