n, m, k = map(int, input().split())
board = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    board[i] = [0] + list(map(int, input().split()))

nxt_board =  [[0]*(n+1) for _ in range(n+1)]
travelers = [(-1,-1)]+[tuple(map(int, input().split())) for _ in range(m)]
exists = tuple(map(int, input().split()))
answer = 0
sx, sy, s_size = 0,0,0

def move_all_traveler():
    global answer
    for i in range(1, m+1):
        if travelers[i] != exists:
            tx, ty = travelers[i]
            ex, ey = exists
            if tx != ex:
                nx, ny = tx, ty
                if ex > nx:
                    nx += 1
                else:
                    nx -= 1
                
                # 상하를 먼저 이동시키므로 벽이 없는 경우 바로 이동시킴
                if not board[nx][ny]:
                    travelers[i] = (nx, ny)
                    answer += 1
                    continue
            if ty != ey:
                nx, ny = tx, ty
                if ey > ny:
                    ny += 1
                else:
                    ny -= 1
                if not board[nx][ny]:
                    travelers[i] = (nx, ny)
                    answer += 1
                    continue        

def find_minimum_square():
    global sx, sy, s_size, exists
    ex, ey = exists
    for sz in range(2, n+1):
        for x1 in range(1, n-sz+2):
            for y1 in range(1, n-sz+2):
                x2, y2 = x1 + sz - 1, y1 + sz - 1
                if not (x1 <= ex <= x2 and y1 <= ey <= y2):continue # 출구가 없는 범위라면
                t_flag = False
                for idx in range(1, m+1):
                    tx, ty = travelers[idx]
                    if ((tx, ty) != (ex, ey)) and (x1 <= tx <= x2 and y1 <= ty <= y2):
                        t_flag = True
                if t_flag:
                    sx = x1
                    sy = y1
                    s_size = sz
                    return 

def rotate_square():
    for x in range(sx, sx+s_size):
        for y in range(sy, sy+s_size):
            if board[x][y]:
                board[x][y] -= 1
            ox, oy = x - sx, y - sy
            rx, ry = oy, s_size - ox - 1
            nxt_board[rx+sx][ry+sy] = board[x][y]
    
    for x in range(sx, sx+s_size):
        for y in range(sy, sy+s_size):
            board[x][y] = nxt_board[x][y]
            
    return

def rotate_traveler_exit():
    global exists

    for i in range(1, m+1):
        tx, ty = travelers[i]
        # 회전시킨 정사각형 안에 있다면 
        if sx <= tx < sx + s_size and sy <= ty < sy + s_size:
            ox, oy = tx-sx, ty-sy
            rx, ry = oy, s_size - ox - 1
            travelers[i] = (rx+sx, ry+sy)
    ex, ey = exists
    if sx <= ex < sx + s_size and sy <= ey < sy + s_size:
        ox, oy = ex-sx, ey-sy
        rx, ry = oy, s_size - ox - 1
        exists = (rx+sx, ry+sy)

for _ in range(k):
    move_all_traveler()

    is_all_escape = True
    for i in range(1, m+1):
        if travelers[i] != exists:
            is_all_escape = False
            break
    if is_all_escape:
        break
    
    find_minimum_square()
    rotate_square()
    rotate_traveler_exit()

print(answer)
ex, ey = exists
print(ex, ey)