import sys
input = sys.stdin.readline 
from collections import deque


BLANK = 0
STONE = 1

n, k, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
start_pos = []
stone_pos = []
answer = 0 # 도달 가능한 칸 수
dxs, dys = [0,0,1,-1], [1,-1,0,0]
for _ in range(k):
    r, c = map(int, input().split())
    start_pos.append((r-1, c-1))

for i in range(n):
    for j in range(n):
        if arr[i][j] == STONE:
            stone_pos.append((i,j))

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def count_can_go(del_stones):
    global arr
    tmp_arr = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp_arr[i][j]=arr[i][j]
    visited = [[False]*n for _ in range(n)]
    cnt = 0

    # 돌을 없앤다
    for del_stone in del_stones:
        del_x, del_y = del_stone
        tmp_arr[del_x][del_y] = BLANK

    # 도달 가능한 곳을 deque로 구한다. 시작 위치는 방문처리
    for pos in start_pos:
        s_x, s_y = pos
        visited[s_x][s_y] = True
        cnt += 1

    que = deque(start_pos)
    while que:
        x, y = que.popleft()
        for d in range(4):
            nx, ny = x +dxs[d], y+dys[d]
            if not in_range(nx, ny):
                continue
            if not visited[nx][ny] and tmp_arr[nx][ny] == BLANK:
                cnt += 1
                visited[nx][ny] = True
                que.append((nx, ny))

    return cnt


def choose_del_stone(depth, selected):
    global answer
    if len(selected) == m:
        answer = max(answer, count_can_go(selected))
        return 
    if depth == len(stone_pos):
        return 

    selected.append(stone_pos[depth])
    choose_del_stone(depth+1, selected)
    selected.pop()

    choose_del_stone(depth+1, selected)

choose_del_stone(0, [])
print(answer)