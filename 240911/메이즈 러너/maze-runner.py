import sys
input = sys.stdin.readline
 
n, m, k = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
runners = {}
for idx in range(1, m+1):
    sr, sc = map(int, input().split())
    runners[idx] = [sr-1, sc-1]
exit = list(map(int, input().split()))
exit[0] -= 1
exit[1] -= 1
escape = [False]*(m+1)
escape[0] = True 
answer = 0

def deep_copy(a):
    return [
        a[i][:]
        for i in range(len(a))
    ]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def runners_move():
    global runners, answer
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    for idx in range(1, m+1):
        if escape[idx]: continue 
        x, y = runners[idx]
        now_dist = abs(exit[0] - x) + abs(exit[1] - y)
        move_dir = -1
        for dir in range(4):
            nx, ny = x + dxs[dir], y + dys[dir]
            if not in_range(nx, ny):continue
            nxt_dist = abs(exit[0] - nx) + abs(exit[1] - ny)
            if (arr[nx][ny] == 0 or [nx, ny] == 0) and nxt_dist < now_dist:
                move_dir = dir
                break
        if  move_dir == -1:continue
        else:
            answer += 1
            runners[idx] = [x + dxs[move_dir], y + dys[move_dir]]
            if runners[idx] == exit:
                escape[idx] = True

def get_smallest_maze():
    for size in range(2, n+1):
        for sx in range(n-size+1):
            for sy in range(n-size+1):
                ex, ey = sx + size, sy + size
                if not(sx <= exit[0] < ex and sy <= exit[1] < ey):
                    continue 

                for idx in range(1, m+1):
                    x, y = runners[idx]
                    if escape[idx]:continue
                    if sx <= x < ex and sy <= y < ey:
                        return (size, sx, sy)

def rotate_maze():
    global runners, arr, exit
    size, sx, sy = get_smallest_maze()
    # print(sx, sy, size)
    nxt_arr = deep_copy(arr)
    
    for i in range(sx, sx + size):
        for j in range(sy, sy + size):
            if arr[i][j]:arr[i][j] -= 1
    
    # 미로 회전 
    for i in range(sx, sx + size):
        for j in range(sy, sy + size):
            ox, oy = i - sx, j - sy
            rx, ry = oy, size - ox - 1
            nxt_arr[rx + sx][ry + sy] = arr[i][j]
    
    arr = deep_copy(nxt_arr)

    # 해당하는 사람도 회전 
    for idx in range(1, m+1):
        if escape[idx]:continue
        x, y = runners[idx]
        if sx <= x < sx + size and sy <= y < sy + size:
            ox, oy = x - sx, y - sy
            rx, ry = oy, size - ox - 1
            runners[idx] = [rx+sx, ry + sy]

    # 출구도 회전 
    x, y = exit
    if sx <= x < sx + size and sy <= y < sy + size:
        ox, oy = x - sx, y - sy
        rx, ry = oy, size - ox - 1
        exit = [rx+sx, ry + sy]


# print(runners)
# runners_move()
# print(runners)
for _ in range(k):
    runners_move()
    # print(runners)

    if all(escape):
        break

    rotate_maze()
    # print(runners)
    # print(exit)
    # print()

print(answer)
print(exit[0]+1, exit[1]+1)