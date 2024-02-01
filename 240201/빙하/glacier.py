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
    visited = [[False]*m for _ in range(n)]
    que.append((0,0))
    visited[0][0] = True
    outer_water_lst = [(0,0)]

    while que:
        x, y = que.popleft()
        for k in range(4):
            nx, ny = x+dxs[k], y+dys[k]
            if not in_range(nx, ny):
                continue
            if not visited[nx][ny]:
                if arr[nx][ny] == WATER:
                    que.append((nx, ny))
                    visited[nx][ny] = True
                    outer_water_lst.append((nx, ny))
    return outer_water_lst

def melt_ice(outer_water):
    global arr
    nxt_arr = [[0]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            nxt_arr[i][j] = arr[i][j] # 녹은 후의 arr를 위한 복사

    for outer_water_pos in outer_water_lst:
        x, y = outer_water_pos
        for k in range(4):
            nx, ny = x+dxs[k], y+dys[k]
            if not in_range(nx, ny):
                continue
            if arr[nx][ny] == ICE:
                nxt_arr[nx][ny] = WATER
    
    # arr에 nxt_arr 복사
    for i in range(n):
        for j in range(m):
            arr[i][j] = nxt_arr[i][j]
    return   

def ice_exist():
    for i in range(n):
        for j in range(m):
            if arr[i][j] == ICE:
                return True
    return False
    
while ice_exist():
    time += 1
    outer_water_lst = get_outer_water()
    last_ice_size = get_ice_size()
    melt_ice(outer_water_lst)

print(time, last_ice_size)