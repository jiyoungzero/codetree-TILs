import sys
input = sys.stdin.readline
from collections import deque

ICE = 1
WATER = 0

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

answer = 0
last_ice_size = 0 
dxs, dys = [0,0,1,-1], [1,-1,0,0]
 
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(sx,sy):
    que = deque()
    que.append((sx, sy))
    visited = [[False]*m for _ in range(n)]
    visited[sx][sy] = True

    outer_ice = [(sx, sy)]
    while que: 
        x, y = que.popleft()
        for k in range(4):
            nx, ny = x +dxs[k], y + dys[k]
            if not in_range(nx, ny):continue
            if not visited[nx][ny] and arr[nx][ny] == WATER:
                que.append((nx, ny))
                visited[nx][ny] = True
                outer_ice.append((nx, ny))

    return outer_ice

def all_melt():
    for i in range(n):
        for j in range(m):
            if arr[i][j] == ICE:
                return False
    return True

while not all_melt():
    outer_ice = bfs(0,0)
    tmp = 0
    for i, j in outer_ice:
        for k in range(4):
            ni, nj = i + dxs[k], j + dys[k]
            if not in_range(ni, nj): continue
            if arr[ni][nj] == ICE:
                arr[ni][nj] = WATER
                tmp += 1
    answer += 1
    last_ice_size = tmp
print(answer, last_ice_size)