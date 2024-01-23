import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
bomb_cols = [int(input()) for _ in range(m)]
dxs, dys = [0, 0,1,-1], [1,-1,0,0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bomb(target_col):
    global arr
    nxt_arr = [row for row in arr]
    x, y, times = 0, 0, 0
    for i in range(n):
        if nxt_arr[i][target_col]:
            x, y, times = i, target_col, nxt_arr[i][target_col]
            break
    for k in range(4):
        for i in range(times):       
            nx, ny = x+dxs[k]*i, y+dys[k]*i
            if not in_range(nx, ny):
                continue
            nxt_arr[nx][ny] = 0

    arr = [row for row in nxt_arr]
    return 

def gravity():
    global arr
    nxt_arr = [[0]*n for _ in range(n)]

    for col in range(n):
        tmp_row = n-1
        for row in range(n-1, -1, -1):
            if arr[row][col]:
                nxt_arr[tmp_row][col] = arr[row][col]
                tmp_row -= 1
    
    arr = [row for row in nxt_arr]
    return 

for b_col in bomb_cols:
    bomb(b_col-1) # 해당 열에서 가장 위에 잇는 십자가 터뜨리기한 후의 결과값 리턴 
    gravity() # 리턴값 x : 중력으로 떨어진 nxt_arr을 arr에 옮김

for row in arr:
    print(*row)