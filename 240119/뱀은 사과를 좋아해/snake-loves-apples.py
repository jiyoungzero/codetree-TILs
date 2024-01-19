import sys
input = sys.stdin.readline 
from collections import deque

APPLE = 1

n, m, k = map(int, input().split())
arr = [[0]*n for _ in range(n)]
answer = 0
direction = {'U': (-1, 0), "D": (1, 0), "R" :(0, 1), "L": (0, -1)}
for _ in range(m):
    x, y = map(int, input().split())
    arr[x-1][y-1] = APPLE
commands = []
for _ in range(k):
    d, p = map(str, input().split())
    commands.append((d, int(p)))

cur_x, cur_y = 0, 0
snake_pos = deque()
snake_pos.append((cur_x, cur_y)) # 뱀의 몸 위치 정보


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def dup_snake_pos(x, y, nxt_pos):
    if nxt_pos == APPLE and (x, y) in snake_pos:
        return True
    if nxt_pos == 0 and (x, y) in list(snake_pos)[1:]:
        return True
    return False    

def update_snake_pos(x, y, eat_flag):
    global snake_pos
    if not eat_flag: # 사과를 먹지 않았을 경우
        if snake_pos: 
            snake_pos.popleft()
        snake_pos.append((x, y))
    else: # 사과를 먹었을 경우 
        snake_pos.append((x, y))


for command in commands:
    d, p = command
    n_dir = direction[d]
    for i in range(p):
        nx, ny = cur_x+n_dir[0], cur_y+n_dir[1]
        
        if not in_range(nx, ny): # 게임이 끝나는 경우, 사과가 잇는 곳일 경우 끝에 포함에서 검사, 아닐 경우 끝은 제외하고 검사
            print(answer+1)
            sys.exit(0)
        if dup_snake_pos(nx, ny, arr[nx][ny]):
            print(answer+1)
            sys.exit(0)


        else:
            if arr[nx][ny] == APPLE:
                update_snake_pos(nx, ny, True)
                arr[nx][ny] = 0
            else:
                update_snake_pos(nx, ny, False)
            answer += 1
            cur_x, cur_y = nx, ny


print(answer)