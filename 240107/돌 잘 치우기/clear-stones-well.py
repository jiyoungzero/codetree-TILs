import sys
input = sys.stdin.readline
from collections import deque

SPACE = 0
STONE = 1

n, k, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
starts = [tuple(map(int, input().split())) for _ in range(k)]
dxs, dys = [0,0,1,-1], [1,-1,0,0]
answer = 0
stones = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == STONE:
            stones.append((i, j))

que = deque()

    
def can_go(a, b, copy_arr, visited):
    if a < 0 or n <= a or b < 0 or n <= b:
        return False
    elif visited[a][b] or copy_arr[a][b] == STONE:
        return False
    return True

def bfs(copy_arr, visited):
    can_go_cnt = 0

    while que:
        x, y = que.popleft()
        for k in range(4):
            nx, ny = x+dxs[k], y+dys[k]
            if can_go(nx, ny, copy_arr, visited):
                que.append((nx, ny))
                can_go_cnt += 1
                visited[nx][ny] = True
    return can_go_cnt

# 백트래킹으로 돌을 적절히 제거한 arr를 리턴하여 bfs를 실행한다. 
def remove_stone(depth, tmp_arr, cnt):
    if cnt == m:
        find_max(tmp_arr)
        return 

    if depth == len(stones):
        return 
    
    # 제거하기
    rx, ry = stones[depth] 
    tmp_arr[rx][ry] = SPACE
    remove_stone(depth+1, tmp_arr, cnt+1)
    tmp_arr[rx][ry] = STONE

    # 제거안하기
    remove_stone(depth+1, tmp_arr, cnt)


def find_max(tmp_arr):
    global answer
    result = 0
    visited = [[False]*n for _ in range(n)]
    for start in starts:
        sx, sy = start
        que.append((sx-1, sy-1))
        visited[sx-1][sy-1] = True
        result += bfs(tmp_arr, visited)
    answer = max(answer, result+1)
    return 
    
tmp_arr = [a[:] for a in arr]
remove_stone(0, tmp_arr, 0)
print(answer)