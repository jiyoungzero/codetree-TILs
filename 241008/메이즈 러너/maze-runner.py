import sys
input = sys.stdin.readline 

BLANK = 0

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
people = {}
moved_dist = 0
is_exited = [False]*(m)

for idx in range(m):
    x, y = map(int, input().split())
    people[idx] = [x-1, y-1]
exit = list(map(int, input().split()))
exit[0],exit[1] = exit[0]-1, exit[1]-1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n 

def people_move():
    global people, moved_dist
    dxs, dys = [0,0,1,-1],[1,-1,0,0]

    for i in range(m):
        if is_exited[i]:continue 
        x, y = people[i]
        final_dir = -1
        original_dist = abs(exit[0] - x) + abs(exit[1] - y)
        shorest_dist = int(1e9)
        for dir in range(4):
            nx, ny = x + dxs[dir], y + dys[dir]
            if not in_range(nx, ny):continue 
            if arr[nx][ny] == BLANK:
                nxt_dist = abs(exit[0] - nx) + abs(exit[1] - ny)
                if original_dist > nxt_dist and nxt_dist <= shorest_dist:
                    shorest_dist = nxt_dist
                    final_dir = dir 
        if final_dir == -1: continue 
        # 움직일 수 있다면 이동 
        people[i] = [x + dxs[final_dir], y + dys[final_dir]]
        moved_dist += 1

        # 출구에 도착했다면 즉시 탈출
        if people[i] == exit:
            is_exited[i] = True 
    # print("moved_people:", people)
    # print("is_exited", is_exited)

def exit_in_size(size, sx, sy):
    return sx <= exit[0] < sx + size and sy <= exit[1] < sy + size

def find_smallest_square():
    for size in range(2, n+1):
        for i in range(n-size+1):
            for j in range(n-size+1):
                # 출구가 포함되는지
                if exit_in_size(size, i, j):
                    # 참가자가 한 명 이상 있는지 
                    ppl_lst = []
                    for idx in range(m):
                        if is_exited[idx]:continue # 이미 탈출한 참가자는 제외 
                        x, y = people[idx]
                        if i <= x < i + size and j <= y < j + size:
                            ppl_lst.append(idx)
                    if len(ppl_lst) > 0:
                        return (size, i, j, ppl_lst)

def deep_copy(a):
    return [
        a[i][:]
        for i in range(len(a))
    ]

def rotate_maze():
    global arr, exit, people
    size, sx, sy, ppl_lst = find_smallest_square()
    nxt_arr = deep_copy(arr)
    # print("moved_dist :", moved_dist )
    # print("rotate (size, sx, sy) :", size, sx, sy)

    for i in range(sx, sx + size):
        for j in range(sy, sy + size):
            oi, oj = i - sx, j - sy
            ri, rj = oj, size - oi - 1
            fi, fj = ri + sx, rj + sy

            # 벽일 때
            if arr[i][j] > 0:
                nxt_arr[fi][fj] = arr[i][j] - 1
            # 벽이 아닐 때
            else:
                nxt_arr[fi][fj] = arr[i][j]
    arr = deep_copy(nxt_arr)

    # 출구 회전 
    ex, ey = exit[0], exit[1]
    oi, oj = ex - sx, ey - sy
    ri, rj = oj, size - oi -1
    fi, fj = ri + sx, rj + sy
    exit = [fi, fj]

    # 그 안의 사람들도 회전 
    for idx in ppl_lst:
        x, y = people[idx]
        oi, oj = x - sx, y - sy
        ri, rj = oj, size - oi - 1
        fi, fj = ri + sx, rj + sy
        people[idx] = [fi, fj]
    # print("people :", people)
    # print("exit :", exit)
    # for row in arr:
    #     print(*row)
    # print()

 
def game_over():
    return all(is_exited)

for _ in range(k):
    people_move()
    if game_over():break
    rotate_maze()

print(moved_dist)
print(exit[0]+1, exit[1]+1)