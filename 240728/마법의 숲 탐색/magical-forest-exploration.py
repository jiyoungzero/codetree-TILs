import sys
input = sys.stdin.readline 
from collections import deque

r, c, k = map(int, input().split())
arr = [[0]*(c) for _ in range(r+3)]
golams = []
for _ in range(k):
    ci, di = map(int, input().split())
    golams.append((ci-1, di))

answer = 0
dxs, dys = [-1, 0,1,0],[0,1,0,-1] # 상좌하우(시계방향)
def in_range(x, y):
    return 0 <= x < r+3 and 0 <= y < c

def can_down(row, col):
    if not (in_range(row+2, col) and in_range(row+1, col-1) and in_range(row+1, col+1)):return False
    return arr[row+2][col] == 0 and arr[row+1][col-1] == 0 and arr[row+1][col+1] == 0

def can_left(row, col):
    if not (in_range(row-1, col-1) and in_range(row, col-2) and in_range(row+1, col-1) and in_range(row+1, col-2) and in_range(row+2, col-1)): return False
    return arr[row-1][col-1] == 0 and arr[row][col-2] == 0 and arr[row+1][col-1] == 0 and arr[row+1][col-2] == 0 and arr[row+2][col-1] == 0

def can_right(row, col):
    if not (in_range(row-1, col+1) and in_range(row, col+2) and in_range(row+1, col+1) and in_range(row+1, col+2) and in_range(row+2, col+1)): return False
    return arr[row-1][col+1] == 0 and arr[row][col+2] == 0 and arr[row+1][col+1] == 0 and arr[row+1][col+2] == 0 and arr[row+2][col+1] == 0

def init_arr():
    global arr
    for i in range(r+3):
        for j in range(c):
            arr[i][j] = 0

def golams_move(idx):
    global arr
    cur_col, exit_d = golams[idx]
    cur_row = 1

    while True:
        # 밑으로 내려가려면
        if cur_row == r+2:break # 바닥까지 간 거라면 
        if can_down(cur_row, cur_col):
            cur_row += 1
            continue
        if can_left(cur_row, cur_col):
            cur_row += 1
            cur_col -= 1
            exit_d = (exit_d - 1)%4
            continue
        if can_right(cur_row, cur_col):
            cur_row += 1
            cur_col += 1
            exit_d = (exit_d + 1)%4
            continue
        break
    # 골렘 최종 위치
    final_row, final_col = cur_row, cur_col

    # 골렘이 숲을 벗어난 상태 -> arr 초기화
    if final_row < 4:
        init_arr()
        return False
    # arr에 골렘 표시
    arr[final_row][final_col] = idx+1
    for dir in range(4):
        nx, ny = final_row + dxs[dir], final_col + dys[dir]
        if dir == exit_d:
            arr[nx][ny] = -(idx+1)
        else:
            arr[nx][ny] = idx+1
    return (final_row, final_col, exit_d) # 정령의 위치
    
def fairy_move(x, y, idx):
    global answer
    visited = [[False]*(c) for _ in range(r+3)]
    que = deque()
    que.append((x, y))
    visited[x][y] = True

    # for row in arr:
    #     print(*row)
    # print()
    while que:
        x, y = que.popleft()    
        
        # 내 위치가 v <0 (출구)이고, 다음 위치가 0이 아닌 값일 때 이동 가능 
        # 내 위치가 v > 0이라면, 다음 위치가 같은 값이여야 이동 가능 + 내 출구면 이동 가능
        for dir in range(4):
            nx, ny = x + dxs[dir], y + dys[dir]
            if not in_range(nx,ny):continue
            if not visited[nx][ny]:
                if arr[x][y] < 0 and arr[nx][ny] != 0:
                    que.append((nx, ny))
                    visited[nx][ny] = True
                if arr[x][y] == abs(arr[nx][ny]):
                    que.append((nx, ny))
                    visited[nx][ny] = True

    for row in range(len(visited)-1, -1, -1):
        if any(visited[row]):
            answer += (row-2)
            break


for i in range(k):
    fairy = golams_move(i)
    if fairy != False: # 정상적으로 위치 잡은 골렘 안의 정령
        fairy_move(fairy[0], fairy[1], i)
print(answer)