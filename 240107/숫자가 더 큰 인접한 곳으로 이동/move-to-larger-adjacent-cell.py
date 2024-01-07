import sys
input = sys.stdin.readline
from collections import deque

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
n, r, c = map(int, input().split())
r -= 1
c -= 1

arr = [list(map(int, input().split())) for _ in range(n)]
visited = [arr[r][c]]
que = deque([(r, c)])

while que:
    r, c = que.popleft()
    for k in range(4):
        nr, nc = r+dxs[k], c+dys[k]
        if nr < 0 or n <= nr or nc < 0 or n <= nc:
            continue
        if arr[nr][nc] > arr[r][c]:
            visited.append(arr[nr][nc])
            que.append((nr, nc))
            break

            

for ele in visited:
    print(ele, end = ' ')