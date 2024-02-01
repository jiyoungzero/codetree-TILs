ICE = 1
WATER = 0
import sys
input = sys.stdin.readline 
from collections import deque


dxs, dys = [0,0,1,-1], [1,-1,0,0]
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
time, last_ice_size = 0, 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def get_ice_size():
    global arr
    result = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == ICE:
                result += 1
    return result

def get_outer_water():
    que = deque()
    outer_water = [[False]*m for _ in range(n)]
    que.append((0,0))
    outer_water[0][0] = True

    while que:
        x, y = que.popleft()
        for k in range(4):
            nx, ny = x+dxs[k], y+dys[k]
            if not in_range(nx, ny):
                continue
            if not outer_water[nx][ny]:
                if arr[nx][ny] == WATER:
                    que.append((nx, ny))
                    outer_water[nx][ny] = True
    return outer_water

def melt_ice(outer_water):
    global arr
    nxt_arr = [[0]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]

    que = deque()
    for i in range(n):
        for j in range(m):
            nxt_arr[i][j] = arr[i][j] # 녹은 후의 arr를 위한 복사
            if outer_water[i][j]:
                que.append((i, j)) # ice를 녹일 수 있는 물
                visited[i][j] = True
    while que:
        x, y = que.popleft()
        for k in range(4):
            nx, ny = x+dxs[k], y+dys[k]
            if not in_range(nx, ny):
                continue
            if arr[nx][ny] == ICE and not visited[nx][ny]:
                nxt_arr[nx][ny] = WATER
                visited[nx][ny] = True
    
    # arr에 nxt_arr 복사
    for i in range(n):
        for j in range(m):
            arr[i][j] = nxt_arr[i][j]
    return   
    
    
while get_ice_size() > 0 :
    time += 1
    outer_water_lst = get_outer_water()
    last_ice_size = get_ice_size()
    melt_ice(outer_water_lst)

print(time, last_ice_size)