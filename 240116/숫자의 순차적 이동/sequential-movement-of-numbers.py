import sys, heapq
input = sys.stdin.readline

dxs, dys = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0<= x < n and 0<= y < n

def turn():
    num_info = {}
    for i in range(n):
        for j in range(n):
            num_info[arr[i][j]] = (i, j)

    for i in range(1,n*n+1):
        x, y = num_info[i]
        max_value, mx, my = 0, 0 ,0
        for k in range(8):
            nx, ny = x+dxs[k], y + dys[k]
            if not in_range(nx, ny):
                continue
            if max_value < arr[nx][ny]:
                mx, my = nx, ny
                max_value = arr[nx][ny]
        arr[mx][my] = i
        arr[x][y] = max_value
        num_info[i] = (mx, my)
        num_info[max_value] = (x, y)

for _ in range(m): # m번의 턴
    turn()


# 출력
for row in arr:
    print(*row)