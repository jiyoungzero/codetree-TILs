n, m, t = map(int, input().split())
BLANK = -1
arr = [[BLANK for _ in range(n)] for _ in range(n)]
nxt_arr = [[BLANK for _ in range(n)] for _ in range(n)]
move_dic = {"U":0, "D":1, 'L': 2, "R":3}

for idx in range(m):
    x, y, d, w = map(str, input().split())
    x, y, d, w =int(x)-1, int(y)-1, move_dic[d], int(w)
    arr[x][y] = [(x, y, w, idx, d)]

def in_range(x,y):
    return 0 <= x < n and 0 <= y < n

def move(x, y):
    global nxt_arr
    dxs, dys = [-1,1,0,0],[0,0,-1,1]
    (x, y, w, ball_idx, d) = arr[x][y][0]
    nx, ny = x +dxs[d], y + dys[d]
    if not in_range(nx, ny):
        d ^= 1        
        # 해당 위치에 구슬이 있는 경우
        if nxt_arr[x][y] != BLANK:
            nxt_arr[x][y].append((nx, ny, w, ball_idx, d))
        # 없는 경우
        else:
            nxt_arr[x][y] = [(nx, ny, w, ball_idx, d)]
    else:
        # 해당 위치에 구슬이 있는 경우
        if nxt_arr[nx][ny] != BLANK:
            nxt_arr[nx][ny].append((nx, ny, w, ball_idx, d))
        # 없는 경우
        else:
            nxt_arr[nx][ny] = [(nx, ny, w, ball_idx, d)]


def move_all():
    for x in range(n):
        for y in range(n):
            if arr[x][y] != BLANK:
                move(x, y)

def collision():
    global nxt_arr, arr
    for x in range(n):
        for y in range(n):
            if nxt_arr[x][y] != BLANK and len(nxt_arr[x][y]) > 1:
                ball_sum, max_ball_idx, max_ball_dir = 0,0,0
                for _, _, w, ball_idx, d in nxt_arr[x][y]:
                    ball_sum += w
                    if max_ball_idx < ball_idx:
                        max_ball_idx = ball_idx
                        max_ball_dir = d
                nxt_arr[x][y] = [(x, y, ball_sum, max_ball_idx, max_ball_dir)]

    # arr에 옮기기
    for x in range(n):
        for y in range(n):
            arr[x][y] = nxt_arr[x][y]
    

def simulate():
    global nxt_arr 
    nxt_arr = [[BLANK for _ in range(n)] for _ in range(n)]
    move_all()
    collision()

for _ in range(t+1):
    simulate()


# 정답 출력
max_weight, cnt = 0, 0
for x in range(n):
    for y in range(n):
        if arr[x][y] != BLANK:
            _, _, w, _, _ = arr[x][y][0]
            cnt += 1
            max_weight = max(max_weight,w)
print(cnt, max_weight)