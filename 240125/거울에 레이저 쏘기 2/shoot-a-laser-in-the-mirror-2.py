import sys
input = sys.stdin.readline

n = int(input())
arr = [ list(input()) for _ in range(n)]
k = int(input())
dxs, dys = [1, 0, -1, 0],[0, 1, 0, -1]  # 아래, 오른쪽, 위, 왼쪽
x, y, cur_dir = 0, 0, 0
if k <= n:
    x = 0
    y = k-1
    cur_dir = 0
elif k > n and k <= 2*n:
    x = (k-n-1)
    y = n-1
    cur_dir = 3
elif k > 2*n and k <= 3*n:
    x = n-1
    y = 3*n - k
    cur_dir = 2
else:
    x = 4*n - k
    y = 0
    cur_dir = 1

answer = 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

while True:
    # print(x, y, cur_dir)
    if arr[x][y] == '/':
        if cur_dir == 0:
            cur_dir = 3 #
        elif cur_dir == 3:
            cur_dir = 0
        elif cur_dir == 1:
            cur_dir = 2
        else:
            cur_dir = 1
    else:#dxs, dys = [0, 1, -1, 0],[1,0,0,-1] # 아래, 오른쪽, 위, 왼쪽
        if cur_dir == 0 : 
            cur_dir = 1 
        elif cur_dir == 1:
            cur_dir = 0
        elif cur_dir == 2:
            cur_dir = 3
        else:
            cur_dir = 2
    nx, ny = x + dxs[cur_dir], y + dys[cur_dir]

    if not in_range(nx, ny):
        break
    x, y = nx, ny
    answer += 1
print(answer)