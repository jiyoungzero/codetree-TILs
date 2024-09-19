import sys
input = sys.stdin.readline 
from collections import deque

n = int(input())
cmds = [tuple(map(int, input().split())) for _ in range(n)]
cmds.sort(key = lambda x : (x[0], -x[1]))
max_row = n
max_col = cmds[-1][1]
arr = [[0]* (300+1) for _ in range(1000+1)]
visited = [[False]*(300+1) for _ in range(1000+1)]
answer = 0

for cmd in cmds:
    s, e = cmd 
    cur_row = 0
    for i in range(max_row):
        flag = True
        cur_row = i
        for j in range(s, e+1):
            if arr[i][j] == 1:
                flag = False
                break
        if flag:
            for j in range(s, e+1):
                arr[cur_row][j] = 1
            break

def in_range(x, y):
    return 0 <= x < 1000+1 and 0 <= y < 300+1

def bfs(sx, sy):
    dxs, dys = [0,0,1,-1], [1, -1,0, 0]
    result = [(sx, sy)]
    que = deque()
    que.append((sx, sy))
    visited[sx][sy] = True 

    while que:
        x, y = que.popleft()
        for dir in range(4):
            nx, ny = x + dxs[dir], y + dys[dir]
            if not in_range(nx, ny):continue 
            if not visited[nx][ny] and arr[nx][ny] == 1:
                result.append((nx, ny))
                visited[nx][ny] = True 
                que.append((nx, ny))
    return result

for i in range(1000+1):
    for j in range(300+1):
        if arr[i][j] == 1 and not visited[i][j]:
            result = bfs(i, j)
            # 제일 작은 행, 제일 큰 행 
            result.sort(key = lambda x : -x[0])
            max_r, min_r = result[0][0], result[-1][0]
            # print(result)
            # 제일 작은 열, 제일 큰 열
            result.sort(key = lambda x : -x[1])
            max_c, min_c = result[0][1], result[-1][1]

            total = (max_r - min_r + 1) * (max_c - min_c + 1)
            answer += (total)
# for row in arr[:15]:
#     print(row[:18])
print(answer)