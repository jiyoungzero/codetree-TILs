from collections import deque
WALL = 1

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
start_spots = deque()
dxs, dys = [0,0,1,-1],[1,-1,0,0]
visited = [[False]*n for _ in range(n)]
answer = 0

for _ in range(k):
    r, c = map(int, input().split())
    start_spots.append((r-1, c-1))
    visited[r-1][c-1] = True

def in_range(x, y):
    return 0<=x<n and 0<= y<n

while start_spots:
    x, y = start_spots.popleft()
    for kk in range(4):
        nx, ny = x + dxs[kk], y + dys[kk]
        if not in_range(nx,ny):
            continue
        if not visited[nx][ny] and arr[nx][ny] != WALL:
            visited[nx][ny] = True
            start_spots.append((nx,ny))

for i in range(n):
    for j in range(n):
        if visited[i][j]:
            answer += 1
print(answer)