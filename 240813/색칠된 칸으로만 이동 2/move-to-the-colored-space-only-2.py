import sys
input = sys.stdin.readline 
from collections import deque

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
painted = [list(map(int, input().split())) for _ in range(m)]
sx, sy = 0, 0

for i in range(m):
    for j in range(n):
        if painted[i][j]:
            sx, sy = i, j
            break

visited = [[False]*n for _ in range(m)]
l, r = 0, 10**9
answer = r 
dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]

def is_connected():
    for i in range(m):
        for j in range(n):
            if painted[i][j] and not visited[i][j]: return False
    return True

def bfs(mid):
    que = deque()
    que.append((sx, sy))
    visited[sx][sy] = True
    
    while que:
        x, y = que.popleft()
        for dir in range(4):
            nx, ny = x+ dxs[dir], y + dys[dir]
            if not (0 <= nx < m and 0 <= ny < n):continue 
            if not visited[nx][ny] and abs(arr[x][y] - arr[nx][ny]) <= mid:
                que.append((nx, ny))
                visited[nx][ny] = True
    return 


def is_possible(target):
    # # init visited
    for i in range(m):
        for j in range(n):
            visited[i][j] = False 

    bfs(target)
                
    return is_connected()


while l <= r:
    mid = (l+r)//2
    if is_possible(mid):
        r = mid - 1
        answer = min(answer, mid)
    else:
        l = mid + 1

print(answer)