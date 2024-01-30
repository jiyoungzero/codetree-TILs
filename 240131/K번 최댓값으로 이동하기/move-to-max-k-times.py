from collections import deque
import heapq
import sys
input = sys.stdin.readline 

dxs, dys = [0,0,1,-1], [1,-1,0,0]
# 숫자가 클수록, 행번호가 작을 수록, 열번호가 작을 수록 
n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r -= 1
c -= 1
que = deque()
f_x, f_y = 0, 0 # 최종 위치

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def find_can_go(num, x, y):
    result = []
    q = deque()
    q.append((x, y))
    visited = [[False]*n for _ in range(n)]
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dxs[d], y + dys[d]
            if not in_range(nx, ny):
                continue
            if visited[nx][ny]:
                continue
            if arr[nx][ny] < num:
                result.append((arr[nx][ny], nx, ny))
                visited[nx][ny] = True
                q.append((nx, ny))
    if result:
        result.sort(key = lambda x : (-x[0], x[1], x[2]))
        return result[0] 
    else:
        return -1
    


def bfs():
    global f_x, f_y, k
    que.append((arr[r][c], r, c, 1))

    while que:
        num, x, y, time = que.popleft()
        result = find_can_go(num, x, y)
        if result == -1:
            f_x, f_y = x, y
            return 
        
        n_num , nx, ny = result
        if time == k:
            f_x, f_y = nx, ny
            return

        que.append((n_num, nx, ny, time + 1))

bfs()
print(f_x+1, f_y+1)