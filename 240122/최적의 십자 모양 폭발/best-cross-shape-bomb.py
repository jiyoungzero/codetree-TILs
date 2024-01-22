import sys
input = sys.stdin.readline

dxs, dys = [0,0,1,-1],[1,-1,0,0]
n = int(input())
answer = 0
arr = [list(map(int, input().split())) for _ in range(n)]
next_arr = [[0]*n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0<= y < n

def bomb(x, y, c_arr):
    bomb_num = c_arr[x][y]
    c_arr[x][y] = 0
    for i in range(1, bomb_num):
        for k in range(4):
            nx, ny = x+dxs[k]*i, y+dys[k]*i
            if not in_range(nx, ny):
                continue
            c_arr[nx][ny] = 0
    return c_arr

def gravity(c_arr):
    # next_arr 초기화
    for i in range(n):
        for j in range(n):
            next_arr[i][j] = 0
    
    # arr을 토대로 next_arr에 중력 받은 걸로 채우기
    for col in range(n):
        tmp_row = n-1
        for row in range(n-1,-1,-1):
            if c_arr[row][col] > 0:
                next_arr[tmp_row][col] = c_arr[row][col]
                tmp_row -= 1
            
    # next_arr를 arr에 옮기기
    for i in range(n):
        for j in range(n):
            c_arr[i][j] = next_arr[i][j]
    return c_arr
    
def find_match(c_arr):
    result = 0
    for x in range(n):
        for y in range(n):
            if c_arr[x][y] > 0:
                for k in range(4):
                    nx, ny = x + dxs[k], y +dys[k]
                    if not in_range(nx, ny):
                        continue
                    if c_arr[x][y] == c_arr[nx][ny]:
                        result += 1
    return result//2


for i in range(n):
    for j in range(n):
        # copy_arr 초기화
        copy_arr = [[0]*n for _ in range(n)]
        for row in range(n):
            for col in range(n):
                copy_arr[row][col] = arr[row][col]

        copy_arr = bomb(i, j, copy_arr)
        copy_arr = gravity(copy_arr)
        answer = max(answer, find_match(copy_arr))


print(answer)