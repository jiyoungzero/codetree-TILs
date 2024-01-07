import sys
input = sys.stdin.readline
from collections import deque

SPACE = 0
STONE = 1

n, k, m = tuple(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
answer = 0
stone_pos = [ (i, j) for i in range(n) for j in range(n) if arr[i][j] == STONE ]
que = deque()
visited = [[False]*n for _ in range(n)]
selected_stones = []

def can_go(x, y):
    if x < 0 or y < 0 or n <= x or n <= y:
        return False
    elif visited[x][y] or arr[x][y] == STONE:
        return False
    return True

def bfs():
    while que:
        x, y = que.popleft()

        dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                que.append((nx, ny))
                visited[nx][ny] = True
    
def calc():
    # 이전 상태를 원상태로 
    for x, y in selected_stones:
        arr[x][y] = SPACE
    
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

    for sx, sy in starts:
        que.append((sx, sy))
        visited[sx][sy] = True
    bfs()

    for x, y in selected_stones:
        arr[x][y] = STONE
    
    can_go_cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                can_go_cnt += 1
    return can_go_cnt


def find_max(depth, cnt):
    global answer
    if cnt == m:
        answer = max(answer, calc())
    if depth == len(stone_pos):
        return 
    
    selected_stones.append(stone_pos[depth])
    find_max(depth + 1, cnt + 1)
    selected_stones.pop()
	
    find_max(depth + 1, cnt)

starts = []
for _ in range(k):
    r, c = tuple(map(int, input().split()))
    starts.append((r - 1, c - 1))
find_max(0,0)
print(answer)