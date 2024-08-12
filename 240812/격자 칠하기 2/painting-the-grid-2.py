import sys
input = sys.stdin.readline 
from collections import deque

n = int(input())
arr= [list(map(int, input().split())) for _ in range(n)]

l, r = 0, 1000000
answer = r 

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(sx, sy, D):
    dxs, dys = [0,0,1,-1], [1,-1,0,0]
    que = deque()
    result = 1
    que.append((sx, sy))
    visited = [[False]*n for _ in range(n)]
    visited[sx][sy] = True
    
    while que:
        x, y = que.popleft()
        for dir in range(4):
            nx, ny = x+ dxs[dir], y + dys[dir]
            if not in_range(nx, ny): continue 
            if not visited[nx][ny] and abs(arr[nx][ny] - arr[x][y]) <= D:
                result += 1
                que.append((nx, ny))
                visited[nx][ny] = True
    return result

def is_possible(target): # d = target 만큼일 때, 시작점에서부터 차이가 d 이하라면 cnt + 1, cnt >= n*n//2 
    for i in range(n):
        for j in range(n):
            cnt = bfs(i, j, target) 
            if n%2 == 0 and cnt >= (n*n)//2:
                return True
            else:
                if cnt >= (n*n+1)//2:
                    return True
    return False

while l <= r:
    mid = (l+r)//2

    if is_possible(mid):
        r = mid - 1
        answer = min(answer, mid)
    else:
        l = mid + 1

print(answer)