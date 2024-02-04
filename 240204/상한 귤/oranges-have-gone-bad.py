import sys
input = sys.stdin.readline 
from collections import deque

BLANK = 0
NORMAL = 1
BAD = 2

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = [[-1]*n for _ in range(n)]
que = deque()
visited = [[-1]*n for _ in range(n)]

def fin_NORMAL():# 끝까지 상하지 않은 귤 -2표시
    global arr, visited
    for i in range(n):
        for j in range(n):
            if arr[i][j] == NORMAL and visited[i][j] == -1:
                visited[i][j] = -2

# 초기 상한 귤 que에 세팅
for i in range(n):
    for j in range(n):
        if arr[i][j] == BAD:
            que.append((i,j))
            visited[i][j] = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs():
    dxs, dys = [0,0,1,-1], [1,-1,0,0]
    while que:
        x, y = que.popleft()
        for d in range(4):
            nx, ny = x + dxs[d], y+ dys[d]
            if not in_range(nx, ny):
                continue
            if visited[nx][ny] == -1 and arr[nx][ny] == NORMAL:
                arr[nx][ny] = BAD
                visited[nx][ny] = visited[x][y] + 1
                que.append((nx, ny))
bfs()
fin_NORMAL()
for ele in visited:
    print(*ele)