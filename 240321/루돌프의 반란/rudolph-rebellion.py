n, m, p, c, d = map(int, input().split())
rudolf = tuple(map(int, input().split()))
arr = [[0]*(n+1) for _ in range(n+1)]
santa_pos = [(0, 0) for _ in range(p+1)]
for _ in range(p):
    pn, sr, sc = map(int, input().split())
    arr[sr][sc] = pn
    pos[pn] = (sr, sc)
is_alive = [True]*(p+1)
is_passout = [0]*(p+1)
santa_score = [0]*(p+1)

def in_range(x, y):
    return 1 <= x < n+1 and 1 <= y < n+1

def rudolf_move():
    global rudolf
    santa_dist = [] # (거리, r, c, move_x, move_y) 
    for i in range(n+1):
        for j in range(n+1):
            move_x, move_y = 0, 0
            if arr[i][j] > 0:
                distance = (i-rudolf[0])**2 + (j-rudolf[1])**2
                if i > rudolf[0]: move_x += 1
                elif i < rudolf[0]: move_x -= 1
                
                if j > rudolf[1]: move_y += 1
                elif j < rudolf[1]: move_y -= 1
                santa_dist.append((distance, i, j, move_x, move_y))
    santa_dist.sort(key = lambda x:(x[0], -x[1], -x[2]))
    _, _, _, move_x, move_y = santa_dist[0]
    rudolf = (rudolf[0]+move_x, rudolf[1]+move_y)

    # 루돌프의 이동으로 산타와 충돌한 경우 
    if arr[rudolf[0]][rudolf[1]] > 0:
        update_flag = True
        # 루돌프와 충돌한 산타 점수 획득 + c
        santa_idx = arr[rudolf[0]][rudolf[1]]
        santa_score[santa_idx] += c
        

        santa_first_x = rudolf[0] + move_x*c
        santa_first_y = rudolf[1] + move_y*c
        print("루돌프 -> 산타", santa_first_x, santa_first_y)
        # 루돌프 충돌로 범위 밖으로 밀려난 경우
        if not in_range(santa_first_x, santa_first_y):
            is_alive[santa_idx] = False
            arr[rudolf[0]][rudolf[1]] = 0
            return 

        santa_last_x, santa_last_y = santa_first_x, santa_first_y
        # 루돌프에 밀려 이동한 곳에 산타가 있을 경우
        if arr[santa_first_x][santa_first_y] > 0:
            while arr[santa_last_x][santa_last_y] > 0:
                santa_last_x += move_x
                santa_last_y += move_y
            # 산타끼리의 상호작용으로 밀려난 곳이 범위 밖인 경우
            if not in_range(santa_last_x, santa_last_y):
                is_alive[santa_idx] = False
                arr[rudolf[0]][rudolf[1]] = 0
                update_flag = False

        if update_flag: # 최종적으로 밀려난 곳이 범위 안일 경우
            # 루돌프와 충돌한 산타 위치 업데이트 
            arr[rudolf[0]][rudolf[1]] = 0
            arr[santa_last_x][santa_last_y] = santa_idx 
            # 루돌프와 충돌한 산타 기절 (i판 부터 i-2까지)
            is_passout[santa_idx] = m-2

    return

    
def santa_move(i, j):
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
    updata_flag = True
    santa_idx = arr[i][j]

    min_dist = (rudolf[0]-i)**2 + (rudolf[1]-j)**2
    move_dir = -1

    for dir in range(4):
        nx, ny = i+dxs[dir], j + dys[dir]
        if not in_range(nx, ny) or arr[nx][ny] > 0:continue
        
        dist = (rudolf[0]-nx)**2 + (rudolf[1]-ny)**2
        if dist < min_dist:
            min_dist = dist
            move_dir = dir
    if move_dir == -1: # 움직일 수 없다면
        return
    else: # 해당 방향으로 움직일 수 있다면
        nx, ny = i + dxs[move_dir], j + dys[move_dir]

        # 위치 업데이트
        arr[i][j] = 0
        arr[nx][ny] = santa_idx

        # 산타의 이동으로 루돌프와 충돌하는 경우
        if rudolf == (nx, ny):
            santa_score[santa_idx] += d 
            # 산타의 반대이동방향        
            reverse_move_dir = (move_dir+2)%4
            santa_first_x = nx + dxs[reverse_move_dir]*d
            santa_first_y = ny + dys[reverse_move_dir]*d 

            # 밀려난 곳이 바로 범위 밖일 경우
            if not in_range(santa_first_x, santa_first_y):
                is_alive[santa_idx] = False
                arr[nx][ny] = 0
                return
                
            while in_range(santa_last_x, santa_last_y) and arr[santa_last_x][santa_last_y] > 0:
                santa_last_x += dxs[reverse_move_dir]
                santa_last_y += dys[reverse_move_dir]
            
            # 연쇄 충돌 발생
            while not (santa_last_x == santa_first_x and santa_last_y == santa_first_y):
                before_x = santa_last_x - dxs[reverse_move_dir]
                before_y = santa_last_y - dys[reverse_move_dir]
                if not in_range(before_x, before_y):break

                idx = arr[before_x][before_y]
                if not in_range(santa_last_x, santa_last_y):
                    is_alive[idx] = False
                else:
                    arr[santa_last_x][santa_last_y] = arr[before_x][before_y]
                    po

    return


def santa_all_move():
    santa_move_list = [0]*(p+1) # 1번부터 순서대로 움직이기 위해 
    for i in range(n+1):
        for j in range(n+1):
            if arr[i][j] > 0 and is_passout[arr[i][j]] == 0: 
                santa_move_list[arr[i][j]] = (i, j)
    
    for i in range(len(santa_move_list)):
        if str(type(santa_move_list[i])) == "<class 'int'>":continue
        santa_move(santa_move_list[i][0], santa_move_list[i][1])

def give_score():
    for i, alive in enumerate(is_alive):
        if alive:santa_score[i] += 1

def is_gameover():
    if m == 0:return True
    for alive in is_alive:
        if alive:return False
    return True

def awake_santa():
    for i in range(p+1):
        if is_passout[i] > 0:
            if is_passout[i] == m: is_passout[i] = 0
def print_arr():
    for i in range(1, n+1):
        for j in range(1, n+1):
            if rudolf == (i,j):
                print(-1, end=" ")
            else:
                print(arr[i][j], end=" ")
        print()
    print()

while True:
    # 기절한 사람이 잇다면 시간에 맞춰서 깨우기
    awake_santa()
    rudolf_move()

    print_arr()
    
    santa_all_move()
    print_arr()
    m -= 1
    give_score()
    # print(*santa_score)
    # print()
    if is_gameover():
        break
    print(m)
    
    
# print(*santa_score)