import sys
input = sys.stdin.readline 
from collections import deque


n, k, u, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0
dxs,dys = [0,0,1,-1],[1,-1,0,0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y  < n

def possible(nx, ny, x, y):
    return u <= abs(arr[x][y]-arr[nx][ny]) <= d

def get_can_go(selected):
    que = deque()
    cnt = 0
    visited = [[False]*n for _ in range(n)]
    for sel in selected:
        x, y = sel
        que.append(sel)
        visited[x][y] = True
        cnt += 1
    
    while que:
        x, y = que.popleft()
        for k in range(4):
            nx, ny = x + dxs[k], y+dys[k]
            if not in_range(nx, ny):
                continue
            if not visited[nx][ny] and possible(nx, ny, x, y):
                visited[nx][ny] = True
                que.append((nx, ny))
                cnt += 1
    return cnt

def choose_cities(depth, selected):
    global answer
    if len(selected) == k:
        answer = max(answer, get_can_go(selected))
        return 
    if depth >= n*n -1 :
        return 
    
    i, j = depth//n, depth%n
    selected.append((i,j))
    choose_cities(depth+1, selected)
    selected.pop()

    choose_cities(depth+1, selected)


choose_cities(0, [])
print(answer)