import sys
input = sys.stdin.readline 

BLANK = 1
SNAKE = 0
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
answer = 0
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] == SNAKE:
        return False
    return True

def dfs(x, y):
    global answer
    dxs, dys = [1,0], [0,1]
    for k in range(2):
        nx, ny = x + dxs[k], y + dys[k]
        if (nx, ny) == (n-1, m-1):
            answer = 1
            return 
        if can_go(nx, ny):
            visited[nx][ny] = True
            dfs(nx, ny)

dfs(0,0)
print(answer)