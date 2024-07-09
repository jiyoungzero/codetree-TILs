import sys
input = sys.stdin.readline 
from collections import deque


dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0] # 오른쪽, 아래, 왼쪽, 위
# 현재 주사위 면 > 격자 판 : 시계방향 + 1
# 현재 주사위 면 == 격자 판 : 그대로
# 현재 주사위 면 < 격자 판 : 반시계 -1

# 주사위 움직임 : 만약 in_range()가 아닐 경우 -> 반대방향으로 바꾼 뒤 & 한 칸 이동

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0
pos = [0,0]
direction = 0
dize = [6, 1, 3, 4, 2, 5] # 바닥, 위, 오른쪽, 왼쪽, 앞, 뒤


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def move_dize():
    global direction, pos, dize

    cur_x, cur_y = pos
    nx, ny = cur_x + dxs[direction], cur_y + dys[direction]
    if not in_range(nx, ny):
        direction = (direction+2)%4
        nx, ny = cur_x + dxs[direction], cur_y + dys[direction]

    if direction == 0:
        n_dize = [dize[2], dize[3], dize[1], dize[0], dize[4], dize[5]]
    elif direction == 1:
        n_dize = [dize[4], dize[5], dize[2], dize[3], dize[1], dize[0]]
    elif direction == 2:
        n_dize = [dize[3], dize[2], dize[0], dize[1], dize[4], dize[5]]
    else:
        n_dize = [dize[5], dize[4], dize[2], dize[3], dize[0], dize[1]]
    
    dize = n_dize
    bottom = dize[0]
    if bottom > arr[nx][ny]:
        direction = (direction + 1)%4
    elif bottom < arr[nx][ny]:
        direction = (direction - 1)%4
    return (nx, ny)

def get_score(sx, sy):
    que = deque()
    que.append((sx, sy))
    visited = [[False]*n for _ in range(n)]
    visited[sx][sy] = True
    target = arr[sx][sy]

    result = target
    while que:
        x, y = que.popleft()
        for dir in range(4):
            nx, ny = x + dxs[dir], y + dys[dir]
            if not in_range(nx, ny):continue 
            if not visited[nx][ny] and target == arr[nx][ny]:
                que.append((nx, ny))
                visited[nx][ny] = True
                result += target
    return result

for _ in range(m):
    nx, ny = move_dize()
    answer += get_score(nx, ny)
    pos = [nx, ny]

print(answer)