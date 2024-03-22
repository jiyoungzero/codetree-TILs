import sys
input = sys.stdin.readline 
from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
max_k = 0
comfort_zone = -1
dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(rain_h, sx, sy):
    global visited
    que = deque()
    que.append((sx, sy))

    visited[sx][sy] = True
    while que:
        x, y = que.popleft()
        for dir in range(4):
            nx, ny = x+ dxs[dir], y + dys[dir]
            if not in_range(nx, ny):continue
            if not visited[nx][ny] and arr[nx][ny] > rain_h:
                visited[nx][ny] = True
                que.append((nx, ny))
                

for rain_h in range(100, 0, -1):
    visited = [[False]*m for _ in range(n)]
    tmp_comfort_zone = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and arr[i][j] > rain_h:
                bfs(rain_h, i, j)
                tmp_comfort_zone += 1
    if comfort_zone <= tmp_comfort_zone:
        comfort_zone = tmp_comfort_zone
        max_k = rain_h
        # print("rain_h", rain_h, tmp_comfort_zone)

print(max_k, comfort_zone)