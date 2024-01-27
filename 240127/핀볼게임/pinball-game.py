import sys
input = sys.stdin.readline 

BLANK = 0
UP_SLASH = 1 # /
DOWN_SLASH = 2 # \

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dxs, dys = [0,0,1,-1], [1,-1,0,0] # 오른쪽, 왼쪽, 아래쪽, 위쪽
answer = 0
cur_dir = 0

def initialize(num):
    if 0<= num <= n:
        x = 0
        y = num-1
        cur_dir = 2
    elif num <= 2*n:
        x = num - n - 1
        y = n-1
        cur_dir = 1
    elif num <= 3*n:
        x = n-1
        y = 3*n - num
        cur_dir = 3
    else:
        x = 4*n - num
        y = 0
        cur_dir = 0
    return (x, y, cur_dir)

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n 

def turn(slash):
    global cur_dir
    if slash == UP_SLASH:
        if cur_dir == 0:
            # dxs, dys = [0,0,1,-1], [1,-1,0,0] # 오른쪽, 왼쪽, 아래쪽, 위쪽
            cur_dir = 3
        elif cur_dir == 1:
            cur_dir = 2
        elif cur_dir == 2:
            cur_dir = 0
        else:
            cur_dir = 1
    else:
        if cur_dir == 0:
            cur_dir = 2
        elif cur_dir == 1:
            cur_dir = 3
        elif cur_dir == 2:
            cur_dir = 1
        else:
            cur_dir = 0
    return cur_dir

# 모든 경우 다 따져보기
for k in range(1, 4*n+1):
    x, y, cur_dir = initialize(k)
    time = 1
    while True:
        nx, ny = x+dxs[cur_dir], y + dys[cur_dir]
        if not in_range(nx, ny):
            time += 1
            break
        if arr[nx][ny] == BLANK:
            x, y = nx, ny
        elif arr[nx][ny] == UP_SLASH:
            x, y = nx, ny
            cur_dir = turn(UP_SLASH)
        else:
            x, y = nx, ny
            cur_dir = turn(DOWN_SLASH)
        time += 1
    answer = max(answer, time)
print(answer)