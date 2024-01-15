import sys
input = sys.stdin.readline


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r -= 1
c -= 1

dxs, dys = [0,0,1,-1],[1,-1,0,0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 터뜨리기
def bomb(x, y):
    times = arr[x][y] - 1
    arr[x][y] = 0 
    for k in range(4):
        tmp = times
        tmp_x, tmp_y = x, y 
        while tmp > 0: 
            tmp -= 1
            nx, ny = tmp_x + dxs[k], tmp_y + dys[k]
            # 범위 내에 있는지
            if not in_range(nx, ny):
                break
            arr[nx][ny] = 0
            tmp_x, tmp_y = nx, ny
            
# 내리기
def down():
    global arr
    tmp_arr = [[0]*n for _ in range(n)]
    for col in range(n):
        t_row = n-1
        for row in range(n-1, -1, -1):
            if arr[row][col] > 0:
                tmp_arr[t_row][col] = arr[row][col]
                t_row -= 1
            else:
                continue

    arr = [row[:] for row in tmp_arr]
    return
                



bomb(r, c)
down()
for row in arr:
    for ele in row:
        print(ele, end =' ')
    print()