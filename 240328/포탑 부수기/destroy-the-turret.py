from collections import deque

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
attack_record = [[[0] for _ in range(m)] for _ in range(n)]
answer = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(attacker, victim):
    global laser_path # 공격자와 피해자를 제외한 최단 경로 (i, j)
    a_x, a_y = attacker
    v_x, v_y = victim

    dxs, dys = [0,1,0,-1],[1,0,-1,0] # 우하좌상
    que = deque()
    visited = [[[] for _ in range(m)] for _ in range(n)]
    que.append((a_x, a_y))
    visited[a_x][a_y] = [(a_x, a_y)]
    
    while que:
        x, y = que.popleft()
        if (x, y) == victim:
            laser_path = visited[x][y][1:-1]
            break

        for dir in range(4):
            nx, ny = x + dxs[dir], y + dys[dir]
            if not in_range(nx, ny):
                nx, ny = nx%n, ny%m
            if len(visited[nx][ny]) ==0 and arr[nx][ny] > 0:
                tmp = visited[x][y] + [(nx, ny)]
                visited[nx][ny] = tmp
                que.append((nx, ny))
    if len(laser_path) > 0:
        return True
    return False


def laser():
    global laser_path, attacker, victim
    a_x, a_y = attacker
    v_x, v_y = victim
    attack = arr[a_x][a_y]

    for p in laser_path:
        x, y = p
        arr[x][y] = max(0, arr[x][y] - attack//2)
    arr[v_x][v_y] = max(0, arr[v_x][v_y] - attack)
    
def potan():
    global potan_path, attacker, victim
    a_x, a_y = attacker
    v_x, v_y = victim
    attack = arr[a_x][a_y]    

    p_dxs, p_dys = [-1,-1,-1,0,0,1,1,1], [-1,0,1,-1,1,-1,0,1]
    for dir in range(8):
        potan_path.append(((v_x+p_dxs[dir])%n, (v_y+p_dys[dir])%m))
    
    for p in potan_path:
        x, y = p
        if (x, y) == attacker:continue
        arr[x][y] = max(0, arr[x][y] - attack//2)
    arr[v_x][v_y] = max(0, arr[v_x][v_y] - attack)

def extra_plus():
    global potan_path, laser_path, attacker, victim
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0:
                if (i, j) not in potan_path and (i, j) not in laser_path and (i, j) != attacker and (i,j) != victim:
                    arr[i][j] += 1

    
def pick(subject):
    lst = [] # (공격력, 최근 공격 경험 -, 행+열 -, 열 -)
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0:
                lst.append((arr[i][j], attack_record[i][j][-1], i+j, j, i))
    lst.sort(key = lambda x : (x[0], -x[1], -x[2], -x[3]))
    if subject == 'attacker':
        tmp = (lst[0][-1], lst[0][-2])
        return tmp
    else:
        tmp = (lst[-1][-1], lst[-1][-2])
        return tmp

def game_over():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0:
                cnt += 1
    if cnt == 1:
        return True
    return False 

def printarr():
    global arr
    for row in arr:
        print(*row)
    print()

for time in range(1, k+1):
    laser_path = [] # 레이저 공격 경로
    potan_path = []
    
    if game_over():
        break

    attacker = pick('attacker') # (x, y, 공격력)
    attack_record[attacker[0]][attacker[1]].append(time)
    victim = pick('victim') # pick_attacker의 반대
    arr[attacker[0]][attacker[1]] += (n+m)

    if bfs(attacker, victim): # 경로가 있다면
        laser()
    else:
        potan() # 경로가 없다면

    # printarr()
    # 포탄 부서짐
    extra_plus() # 관계없는 포탑은 +1 공격력 
    # printarr()

for row in arr:
    answer = max(answer, max(row))

print(answer)