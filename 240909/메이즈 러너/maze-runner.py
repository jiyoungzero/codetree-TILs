import sys
input = sys.stdin.readline 

EXIT = -2
n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ppl = []
for _ in range(m):
    x, y = map(int, input().split())
    ppl.append([x-1, y-1])
ex, ey = map(int, input().split())
arr[ex-1][ey-1] = EXIT

answer = 0
escape = [False]*m

def deep_copy(a):
    return [
        a[i][:]
        for i in range(len(a))
    ]

def find_exit():
    for i in range(n):
        for j in range(n):
            if arr[i][j] == EXIT:
                return (i, j)

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n 

def ppl_move():
    global answer, ppl
    nxt_ppl = deep_copy(ppl)
    ex, ey = find_exit()
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1] # 상 하 좌 우

    for idx, person in enumerate(ppl):
        if escape[idx]: continue
        x, y = person
        move_dir = -1
        now_dist = abs(ex-x) + abs(ey-y)
        # 상하
        flag = False # 상하 중에서 이미 갈 수 있는 곳이 있는지 판별 
        for dir in range(2):
            nx, ny = x + dxs[dir], y + dys[dir]
            if not in_range(nx, ny):continue 
            if arr[nx][ny] <= 0:
                nxt_dist = abs(ex-nx) + abs(ey - ny)
                if nxt_dist < now_dist:
                    move_dir = dir
                    flag = True
                    break
                    
        if not flag:
            # 좌우
            for dir in range(2, 4):
                nx, ny = x + dxs[dir], y + dys[dir]
                if not in_range(nx, ny):continue 
                if arr[nx][ny] <= 0:
                    nxt_dist = abs(ex-nx) + abs(ey - ny)
                    if nxt_dist < now_dist:
                        move_dir = dir
                        break
        # 움직일 곳이 없다면
        if move_dir == -1:
            continue 
        # 움직일 곳이 있다면
        else:
            fx, fy = x + dxs[move_dir], y + dys[move_dir]
            nxt_ppl[idx] = [fx, fy]
            answer += 1
        
    ppl = deep_copy(nxt_ppl)
    for idx, (x, y) in enumerate(ppl):
        if x == ex and y == ey: escape[idx] = True

    # print(ppl, escape)

def find_smallest_maze():
    for size in range(2, n+1):
        for si in range(n-size+1):
            for sj in range(n-size+1):
                cnt = 0
                flag = False # 현재까지 미로를 찾았는지
                for i in range(si, si+size):
                    for j in range(sj, sj+size):
                        if [i, j] in ppl and not escape[ppl.index([i, j])]:cnt += 1
                        if arr[i][j] == EXIT : flag = True
                if cnt >= 1 and flag:
                    return (size, si, sj)
            
def rotate_maze():
    global arr, ppl
    size, sx, sy = find_smallest_maze()
    # print(size, sx, sy)
    r_arr = deep_copy(arr) 
    nxt_ppl = deep_copy(ppl)
    for i in range(sx, sx+size):
        for j in range(sy, sy+size):
            oi, oj = i - sx, j - sy
            ri, rj = oj, size - oi - 1
            ri += sx
            rj += sy 
            # 사람도 회전
            if [i, j] in ppl:
                # print(ppl, [i,j], "is in ppl")
                idx = ppl.index([i, j])
                nxt_ppl[idx] = [ri, rj]
            if arr[i][j] > 0:
                r_arr[ri][rj] = arr[i][j] - 1
            else:
                r_arr[ri][rj] = arr[i][j]

    arr = deep_copy(r_arr)
    ppl = deep_copy(nxt_ppl)


def game_over():
    return all(escape)

for _ in range(k):
    if game_over():break 
    ppl_move()
    rotate_maze()



print(answer)
ex, ey = find_exit()
print(ex+1, ey+1)

# for row in arr:
#     print(*row)
# print()
# rotate_maze()
# for row in arr:
#     print(*row)
# print()