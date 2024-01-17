import sys
from collections import deque
input = sys.stdin.readline 

WALL = '#'
BLANK = '.'

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0] # R - D - L - U
n = int(input())
start_x, start_y = map(int, input().split())
arr = [input().rstrip() for _ in range(n)]
start_x -= 1
start_y -= 1
check_dir = 1 # D
cur_dir = 0 # R
answer = 1

def in_range(x, y):
    return 0 <= x < n and 0<= y < n

def simulate(sx, sy):
    global check_dir, cur_dir, answer
    que = deque()
    que.append((sx, sy))
    if arr[1][0] == BLANK:return -1
    while que:
        x, y = que.popleft()
        nx, ny = x+dxs[cur_dir], y+dys[cur_dir]
        dx, dy = x+dxs[check_dir], y+dys[check_dir] # 벽짚은 곳

        # print("현재 위치=(",x, y,") 아랫위치 = (", dx, dy,") 직진위치 = (", nx, ny, ")" )

        if arr[dx][dy] == WALL and arr[nx][ny] == WALL:# 반시계 전환 
            check_dir = (check_dir+3)%4
            cur_dir = (cur_dir+3)%4
            nx, ny = x+dxs[cur_dir], y+dys[cur_dir]
            dx, dy = x+dxs[check_dir], y+dys[check_dir]
        if (arr[dx][dy] == BLANK and not in_range(nx, ny)) \
        or ( arr[dx][dy] == BLANK and arr[nx][ny] == BLANK): # 시계 전환
            check_dir = (check_dir+1)%4
            cur_dir = (cur_dir+1)%4
            nx, ny = x+dxs[cur_dir], y+dys[cur_dir]
            dx, dy = nx+dxs[check_dir], ny+dys[check_dir]

        if (arr[dx][dy] == WALL and not in_range(nx, ny)): # 탈출
            return answer

        elif arr[dx][dy] == WALL and arr[nx][ny] == BLANK: # 직진
            que.append((nx, ny))
            answer += 1
    return -1


print(simulate(start_x, start_y))