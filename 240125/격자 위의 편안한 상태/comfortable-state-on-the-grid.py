n, m = map(int ,input().split())
cmd = [list(map(int, input().split())) for _ in range(m)]
arr = [[0]*n for _ in range(n)]
dxs, dys = [0,0,1,-1],[-1,1,0,0]

def in_range(a, b):
    return 0<=a<n and 0<=b<n

def comfotable(x, y):
    flag = 0
    for k in range(4):
        nx, ny =x+dxs[k], y+dys[k]
        if in_range(nx, ny) and arr[nx][ny] == 1:
            flag += 1
    if flag == 3:
        return True
    else:
        return False


for c in cmd:
    r, c = c[0]-1, c[1]-1
    arr[r][c] = 1
    if comfotable(r, c):
        print(1)
    else:
        print(0)