from collections import deque
import sys
input = sys.stdin.readline 

SNAKE = 0
BLANK = 1
dxs, dys = [0,0,1,-1], [1,-1,0,0]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
que = deque()
visited = [[False]*m for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs():
    que.append((0,0)) # 시작 위치
    visited[0][0] = True
    while que:
        x, y = que.popleft()
        for k in range(4):
            nx, ny = x+dxs[k], y+dys[k]
            if nx == (n-1) and ny == (m-1):
                print(1)
                return 
            if not in_range(nx, ny):
                continue
            if not visited[nx][ny] and arr[nx][ny] == BLANK:
                visited[nx][ny] = True
                que.append((nx, ny))
    print(0)
    return 

bfs()