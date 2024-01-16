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
check_dir = 1
cur_dir = 0 # 전환 시, (cur_dir+1)%4
answer = 0 

def in_range(x, y):
    return 0 <= x < n and 0<= y < n

def simulate(sx, sy):
    global check_dir, cur_dir, answer
    que = deque()
    que.append((sx, sy))
    while que:
        x, y = que.popleft()
        print(x, y)
        nx, ny = x+dxs[cur_dir], y+dys[cur_dir]
        if not in_range(nx, ny): # 탈출
            answer += 1
            return answer

        if arr[nx][ny] == WALL:# 방향 전환 - 직진
            check_dir = (check_dir+1)%4
            cur_dir = (cur_dir+1)%4
            que.append((x, y))
        
        elif arr[nx][ny] == BLANK:
            que.append((nx, ny))
            answer += 1
    return -1


print(simulate(start_x, start_y))