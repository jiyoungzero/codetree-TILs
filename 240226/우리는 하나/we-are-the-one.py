import sys
input = sys.stdin.readline 
from collections import deque
from itertools import combinations

dxs, dys = [0,0,1,-1],[1,-1,0,0]
n, k, u, d = map(int, input().split())
answer = -1
arr = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(selected):
    que = deque(selected)
    cnt = k 
    visited = [[False]*n for _ in range(n)]
    for sel in selected:
        i, j = sel
        visited[i][j] = True

    while que:
        x, y = que.popleft()
        for dirc in range(4):
            nx, ny = x + dxs[dirc], y + dys[dirc]
            if not in_range(nx, ny):
                continue 
            if not visited[nx][ny] and u <= abs(arr[nx][ny] - arr[x][y]) <= d:
                visited[nx][ny] = True
                que.append((nx, ny)) 
                cnt += 1
    return cnt 
coords = [(x, y) for x in range(n) for y in range(n)]
lst = list(combinations(coords, k))
for ele in lst:
    answer = max(answer, bfs(ele))
print(answer)