import sys
input = sys.stdin.readline

n,m,q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
winds = []
nxt_arr = [[0]*m for _ in range(n)]
for_avg_arr = [[0]*m for _ in range(n)]

for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    winds.append((r1-1,c1-1, r2-1, c2-1))

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m 

def rotate(wind):
    global arr, nxt_arr, for_avg_arr
    for i in range(n):
        for j in range(m):
            nxt_arr[i][j] = arr[i][j]
    r1, c1, r2, c2 = wind

    # 오른쪽 이동
    nxt_arr[r1][c1+1:c2+1] = arr[r1][c1:c2]

    # 아래쪽 이동
    for row in range(r1, r2):
        nxt_arr[row+1][c2] = arr[row][c2]

    # 왼쪽 이동
    nxt_arr[r2][c1:c2] = arr[r2][c1+1:c2+1]

    # 위쪽 이동
    for row in range(r2-1, r1-1,-1):
        nxt_arr[row][c1] = arr[row+1][c1]

    for i in range(n):
        for j in range(m):
            for_avg_arr[i][j] = nxt_arr[i][j]

def get_average(x, y):
    result = nxt_arr[x][y]
    cnt = 1
    dxs, dys = [0,0,1,-1], [1, -1, 0, 0]
    for k in range(4):
        nx, ny = x +dxs[k], y + dys[k]
        if in_range(nx, ny):
            result += for_avg_arr[nx][ny]
            cnt += 1
    return result // cnt


def change_avg(wind):
    global arr, nxt_arr
    r1, c1, r2, c2 = wind
    
    for row in range(r1, r2+1):
        for col in range(c1, c2+1):
            nxt_arr[row][col] = get_average(row, col)
    
    for i in range(n):
        for j in range(m):
            arr[i][j] = nxt_arr[i][j]


for wind in winds:
    rotate(wind)
    change_avg(wind)

for row in arr:
    print(*row)