import sys
input = sys.stdin.readline 
from collections import deque

BLANK = 0
WALL = 1
PERSON = 2
SAFE = 3
dxs, dys = [0,0,1,-1], [1,-1,0,0]

n, h, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
que = deque()
answer = [[0]*n for _ in range(n)]
visited = [[False]*n for _ in range(n)]
# 모든 연산이 끝난 후에도 safe zone에 못 간 사람은 -1
def final():
    global answer, arr
    for i in range(n):
        for j in range(n):
            if arr[i][j] == PERSON and answer[i][j] == 0:
                answer[i][j] = -1




def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(i,j,route):
    global answer
    si, sj = i, j
    while que:
        x, y,route = que.popleft()
        if arr[x][y] == SAFE:
            answer[si][sj] = route
            return 

        for d in range(4):
            nx, ny = x + dxs[d], y + dys[d]
            if not in_range(nx, ny):
                continue
            if arr[nx][ny] != WALL and not visited[nx][ny]:
                visited[nx][ny] = True
                que.append((nx, ny,route+1))



# 사람이 있는 곳 저장
for i in range(n):
    for j in range(n):
        if arr[i][j] == PERSON:
            que = deque()
            que.append((i,j,0))
            visited = [[False]*n for _ in range(n)]
            visited[i][j] = True
            bfs(i,j,0)
final()
for row in answer:
    print(*row)