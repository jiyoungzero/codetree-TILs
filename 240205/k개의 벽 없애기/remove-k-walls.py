import sys
input = sys.stdin.readline 
from collections import deque

dxs, dys= [0,0,1,-1],[1,-1,0,0]
WALL = 1
BLANK = 0

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
r1, c1, r2, c2 = r1-1, c1-1, r2-1, c2-1
answer = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs():
    global k, answer, r1, c1, r2, c2
    que = deque()
    visited = [[-1]*n for _ in range(n)]
    visited[r1][c1] = 0

    que.append((r1, c1, 0)) 
    while que:
        x, y, break_wall = que.popleft()

        if break_wall <= k and x == r2 and y == c2:
            answer = visited[x][y]
            return True
        if break_wall > k and x == r2 and y == c2:  
            return False

        for d in range(4):
            nx, ny = x + dxs[d], y + dys[d]
            if not in_range(nx, ny):
                continue
            if arr[nx][ny] == WALL and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                arr[nx][ny] = BLANK
                que.append((nx, ny, break_wall+1))
            elif arr[nx][ny] == BLANK and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                que.append((nx, ny, break_wall)) 

if bfs():
    print(answer)
else:
    print(-1)