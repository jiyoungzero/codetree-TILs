import sys
input = sys.stdin.readline 
from collections import deque

SNAKE = 0
BLACK = 1
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dxs, dys = [0,0,1,-1],[1,-1,0,0]
visited = [[False]*m for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0<= y < m

def bfs():
    que = deque()
    que.append((0, 0))
    while que:
        x, y = que.popleft()
        for k in range(4):
            nx, ny = x+dxs[k], y+dys[k]
            if (nx, ny) == (n-1, m-1):
                return arr[x][y]

            if in_range(nx, ny):
                if not visited[nx][ny] and arr[nx][ny] == BLACK:
                    visited[nx][ny] = True
                    arr[nx][ny] = arr[x][y]+1
                    que.append((nx, ny))
    return -1


print(bfs())