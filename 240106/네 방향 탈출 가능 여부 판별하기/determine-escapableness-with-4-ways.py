import sys
input = sys.stdin.readline
from collections import deque

BLANK = 1
SNAKE = 0
VISITED = 2

n, m = map(int, input().split())
arr = [ list(map(int, input().split())) for _ in range(n)]
answer = 0 # 탈출 할 수 없으면 0, 있으면 1
que = deque()
dxs, dys = [0, 0,1, -1], [1,-1,0,0]
    

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    if arr[x][y] == VISITED or arr[x][y] == SNAKE:
        return False
    return True


def bfs(cur_x, cur_y):
    global answer
    que.append((cur_x, cur_y))
    arr[cur_x][cur_y] = VISITED

    while que:
        x, y = que.popleft()
        if (x, y) == (n-1, m-1):
            answer = 1
            return 
        for k in range(4):
            nx, ny = x+dxs[k], y +dys[k]
            if can_go(nx, ny):
                que.append((nx, ny))

bfs(0 ,0)
print(answer)