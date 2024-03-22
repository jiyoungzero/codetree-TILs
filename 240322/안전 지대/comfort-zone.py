import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
k = 0
comfort_zone = -1
dxs, dys = [0,0,1,-1], [1,-1,0,0]

def dfs(rain_h, x, y):
    if not (0<=x<n and 0<=y<m):return False
    if not visited[x][y] and arr[x][y] > rain_h:
        visited[x][y] = True
        for dir in range(4):
            nx, ny = x + dxs[dir], y + dys[dir]
            dfs(rain_h, nx, ny)
        return True
    return False

for rain_h in range(100, 0, -1):
    tmp_comfort_zone = 0
    visited = [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if dfs(rain_h, i, j):
                tmp_comfort_zone += 1
    if tmp_comfort_zone >= comfort_zone:
        comfort_zone = tmp_comfort_zone
        k = rain_h

print(k, comfort_zone)