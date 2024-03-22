import sys
input = sys.stdin.readline 
from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dxs, dys = [0,0,1,-1], [1,-1,0,0]
bomb_cnt, max_block = 0, 0
visited = [[False]*n for _ in range(n)]

def bfs(sx, sy):
    global visited
    que = deque()
    size = 1
    que.append((sx, sy))
    visited[sx][sy] = True

    while que:
        x, y = que.popleft()
        for k in range(4):
            nx, ny = x + dxs[k], y + dys[k]
            if not (0 <= nx < n and 0 <= ny < n):continue
            if not visited[nx][ny]:
                if arr[sx][sy] == arr[nx][ny]:
                    visited[nx][ny] = True
                    size += 1
                    que.append((nx, ny))
    return size

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            block_size = bfs(i, j)
            if block_size >= 4: bomb_cnt += 1
        max_block = max(max_block, block_size)
print(bomb_cnt, max_block)