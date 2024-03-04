import sys
input = sys.stdin.readline
from collections import deque

ICE = 1
WATER = 0

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

answer = 0
dxs, dys = [0,0,1,-1], [1,-1,0,0]
 
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def surround_ice(x, y):
    cnt = 0
    for k in range(4):
        nx, ny = x + dxs[k], y + dys[k]
        if in_range(nx, ny):
            if arr[nx][ny] == ICE:
                cnt += 1
    return True if cnt == 4 else False

def get_outer_ice(): # 겉면의 빙하 저장
    q = deque()
    visited = [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] == WATER and not surround_ice(i, j):
                for k in range(4):
                    ni, nj = i + dxs[k], j + dys[k]
                    if in_range(ni,nj):
                        if not visited[ni][nj] and arr[ni][nj] == ICE:
                            q.append((ni, nj))
                            visited[ni][nj] = True
    return q

def all_melt():
    for i in range(n):
        for j in range(m):
            if arr[i][j] == ICE:
                return False
    return True

last_ice_size = 0
while not all_melt():
    que = get_outer_ice()
    last_ice_size = len(que)
    for x, y in que:
        arr[x][y] = WATER
    answer += 1
print(answer, last_ice_size)