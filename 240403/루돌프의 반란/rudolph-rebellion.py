import sys
input = sys.stdin.readline 

N, M, P, C, D = map(int, input().split())
rudolf = tuple(map(int, input().split()))
rudolf = (rudolf[0]-1, rudolf[1]-1)
arr = [[0]*N for _ in range(N)]

santas = [[] for _ in range(P+1)]
for _ in range(P):
    pn, sr, sc = map(int, input().split())
    santas[pn] = [sr-1, sc-1]
    arr[sr-1][sc-1] = pn 
scores = [0]*(P+1)
is_dead = [False]*(P+1) 
is_passout = [0]*(P+1) 
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1] # 상우하좌
arr[rudolf[0]][rudolf[1]] = -1

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

def move_rudolf(time):
    global rudolf, is_dead, is_passout, scores
    dist = []
    
    for i in range(1, P+1):
        if i == 0:continue
        if is_dead[i]:continue
        x, y = santas[i]
        dx, dy = 0, 0
        if x > rudolf[0]:
            dx += 1
        elif x < rudolf[0]:
            dx -= 1
        
        if y > rudolf[1]:
            dy += 1
        elif y < rudolf[1]:
            dy -= 1
        dist.append([(x - rudolf[0])**2 + (y-rudolf[1])**2, x, y, dx, dy])

    dist.sort(key = lambda x : (x[0], -x[1], -x[2]))

    # 루돌프 이동방향 
    dx, dy = dist[0][3], dist[0][4]
    arr[rudolf[0]][rudolf[1]] = 0
    rudolf = (rudolf[0] + dx, rudolf[1] + dy)

    if arr[rudolf[0]][rudolf[1]] > 0: # 루돌프가 이동한 곳에 산타가 있다면 
        target_santa_idx = arr[rudolf[0]][rudolf[1]]
        

        scores[target_santa_idx] += C 
        is_passout[target_santa_idx] = time + 1

        first_x, first_y = rudolf[0]+(dx*C), rudolf[1]+(dy*C)
        last_x, last_y = first_x, first_y

        while in_range(last_x, last_y) and arr[last_x][last_y] > 0: # 산타의 상호작용 - 밀림
            last_x += dx
            last_y += dy

        while last_x != first_x or last_y != first_y:
            prev_x = last_x - dx
            prev_y = last_y - dy
            idx = arr[prev_x][prev_y]
            
            if not in_range(last_x, last_y):
                is_dead[idx] = True
            else:        
                arr[last_x][last_y] = arr[prev_x][prev_y]
                last_x, last_y = prev_x, prev_y 

        if not in_range(first_x, first_y):
            is_dead[target_santa_idx] = True
        else:
            arr[first_x][first_y] = target_santa_idx

    update_santas_pos()
    arr[rudolf[0]][rudolf[1]] = -1
    # print(santas, rudolf)
    return 

def update_santas_pos():
    global santas
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0 and not is_dead[arr[i][j]]:
                santas[arr[i][j]] = [i, j]
    return 


def all_move_santa(time):
    # time+1보다 큰 기절 안한 산타만 이동
    global santas, is_dead, is_passout
    for i in range(1, P+1):
        if is_dead[i] or is_passout[i] >= time:
            continue 
        # 산타 이동 
        santa = santas[i]
        x, y = santa
        dx, dy = 0, 0
        min_dist = (rudolf[0]-x)**2 + (rudolf[1]-y)**2
        for dir in range(4):
            nx, ny = x + dxs[dir], y + dys[dir]
            if not in_range(nx, ny) or arr[nx][ny] > 0:
                continue
            dist = (rudolf[0]-nx)**2 + (rudolf[1]-ny)**2
            if min_dist > dist:
                dx, dy = dxs[dir], dys[dir]
                min_dist = dist
        # 루돌프와 충돌하는 경우
        if arr[x+dx][y+dy] == -1 :
            arr[x][y] = 0
            is_passout[i] = time + 1
            scores[i] += D 

            r_dx = dx *(-1)
            r_dy = dy *(-1)

            first_x, first_y = x+dx + (r_dx*D), y+dy+(r_dy*D)  # 루돌프와 충돌로 밀려난 곳
            last_x, last_y = first_x, first_y

            while in_range(last_x, last_y) and arr[last_x][last_y] > 0: # 다른 산타와의 상호작용
                last_x += r_dx
                last_y += r_dy

            while last_x != first_x or last_y != first_y:
                prev_x = last_x - r_dx
                prev_y = last_y - r_dy

                idx = arr[prev_x][prev_y]
                if not in_range(last_x, last_y):
                    is_dead[idx] = True
                else:
                    arr[last_x][last_y] = idx
                last_x, last_y = prev_x, prev_y
                
            
            if not in_range(first_x, first_y):
                is_dead[i] = True
            else:
                arr[first_x][first_y] = i
        else:
            arr[x][y] = 0
            first_x = x + dx
            first_y = y + dy
            arr[first_x][first_y] = i 
            

    update_santas_pos()
    # for i in range(1, P+1):
    #     if not is_dead[i]:
    #         print(santas[i])
    return

def game_over():
    for i in range(1, P+1):
        if not is_dead[i]:
            return False
    return True

def extra_plus():
    global scores
    for i in range(1, P+1):
        if not is_dead[i]:
            scores[i] += 1
    return


for time in range(1, M+1):
    if game_over():
        break 
    move_rudolf(time)
    all_move_santa(time) # 충돌, 기절, 상호작용 해결하기
    
    extra_plus()
print(*scores[1:])