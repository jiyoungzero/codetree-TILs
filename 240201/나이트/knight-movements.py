import sys
input = sys.stdin.readline 
from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
visited = [[False]*(n+1) for _ in range(n+1)]
answer = -1
dxs, dys = [-1,-2,-2,-1,1,2,2,1],[-2,-1,1,2,-2,-1,1,2]
def in_range(x, y):
    return 1 <= x < n+1 and 1 <= y < n+1

def bfs():
    global answer
    que = deque()
    que.append((r1, c1, 1))
    visited[r1][c1] = True

    while que:
        x, y, cnt = que.popleft()
        for k in range(8):
            nx, ny = x+dxs[k], y + dys[k]
            if (nx == r2) and (ny == c2):
                answer = cnt
                return 
            if not in_range(nx, ny):
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = True
                que.append((nx, ny, cnt + 1))
    return 

bfs()
print(answer)