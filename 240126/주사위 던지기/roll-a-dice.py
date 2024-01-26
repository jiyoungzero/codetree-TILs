import sys
input = sys.stdin.readline

n, m, r, c = map(int, input().split())
r -= 1
c -= 1
arr = [[0]*n for _ in range(n)]
commands = list(input().split())
dice = [1,6,3,4,2,5] # 위, 바닥, 오른쪽, 왼쪽, 앞, 뒤
dirc = {'L': 0, 'R':1, 'U':2, "D":3 }
dxs, dys = [0,0,-1,1], [-1,1,0,0]
dice_x, dice_y = 1, 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def write(x, y, cur_dir):# (x, y)에다가 현재 주사위 아랫면 값을 적기
    global arr 
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if cur_dir == 2:
        dice[5], dice[4], dice[2], dice[3], dice[0], dice[1] = a, b, c, d, e, f
    elif cur_dir == 1:
        dice[2], dice[3], dice[1], dice[0], dice[4], dice[5] = a, b, c, d, e, f 
    elif cur_dir == 0:
        dice[3], dice[2], dice[0], dice[1], dice[4], dice[5] = a, b, c, d, e, f 
    else:
        dice[4], dice[5], dice[2], dice[3], dice[1], dice[0] = a, b, c, d, e, f 
    arr[x][y] = dice[1] # idx =1 이 바닥

    return 
    
def roll(cmd):
    global r, c
    cur_dir = dirc[cmd]
    nr, nc = r + dxs[cur_dir], c + dys[cur_dir]
    if not in_range(nr, nc):
        return # 무시
    write(nr, nc, cur_dir)
    r, c = nr, nc
    return 


# 초기 위치에 먼저 arr기록
arr[r][c] = 6
for cmd in commands:
    roll(cmd)

answer = 0
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            answer += arr[i][j]
print(answer)