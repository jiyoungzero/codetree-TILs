import sys
import math
input = sys.stdin.readline 

# 좌하우상
dxs, dys = [0, 1, 0, -1], [-1, 0, 1, 0]
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# 기존의 먼지 양에 더해지고
# 빗자루가 이동한 위치(Curr)에 있는 먼지는 모두 없어지게 됩니다. 
# a = cur - 이동을 완료한 양 = 남은 양
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def swipe(sx, sy, nx, ny):
    global arr, answer
    # sdx, sdy를 2차원 배열로 만들기
    dust_dxs_dys = [[[-2, -1, -1, -1, 0, 1, 1, 1, 2, 0], [0, -1, 0, 1, -2, -1, 0, 1, 0, -1]],
    [[0, 1, 0, -1, 2, 1, 0, -1, 0, 1], [-2, -1, -1, -1, 0, 1, 1, 1, 2, 0]],
    [[-2, -1, -1, -1, 0, 1, 1, 1, 2, 0], [0, 1, 0, -1, 2, 1, 0, -1, 0, 1]],
    [[0, -1, 0, 1, -2, -1, 0, 1, 0, -1], [2, 1, 1, 1, 0, -1, -1, -1, -2, 0]]]
    prop = [0.02, 0.1, 0.07, 0.01, 0.05, 0.1, 0.07, 0.01, 0.02]
    sand = arr[nx][ny]
    for k in range(9):
        sdx, sdy = dust_dxs_dys[dir]
        nnx, nny = nx + sdx[k], ny + sdy[k]
        move = math.floor(sand * prop[k])
        if not in_range(nnx, nny):
            answer += move 
        else:
            arr[nnx][nny] += move 
        arr[nx][ny] -= move 
    # a% 
    sdx, sdy = dust_dxs_dys[dir]
    nnx, nny = nx + sdx[-1], ny + sdy[-1]
    if not in_range(nnx, nny):
        answer += arr[nx][ny]
    else:
        arr[nnx][nny] += arr[nx][ny]
    arr[nx][ny] = 0

    return 

answer = 0
x, y = n//2, n//2
times = 0
dir = 0
while (x, y) != (0, 0):
    if dir%2 == 0:
        times += 1
    for _ in range(times):
        nx, ny = x + dxs[dir], y + dys[dir]
        swipe(x, y, nx, ny)
        x, y = nx, ny
        if (x, y) == (0, 0):break
    dir = (dir+1)%4

print(answer)