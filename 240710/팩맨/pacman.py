import sys
input = sys.stdin.readline 

n = 4
m, t = map(int ,input().split())
t_num = 1 # 현재 턴

px, py = map(int ,input().split())
px -= 1
py -= 1

# 몬스터를 위한 방향
dxs = [-1, -1,  0,  1, 1, 1, 0, -1]
dys = [ 0, -1, -1, -1, 0, 1, 1,  1]

# 팩맨을 위한 방향 : 상좌하우 순
p_dxs = [-1,  0, 1, 0]
p_dys = [ 0, -1, 0, 1]


# t턴에 (x, y) 위치의 move_dir를 바라보는 몬스터의 수
monster = [
    [
        [
            [0]*8
            for _ in range(n)
        ]
        for _ in range(n)
    ]

    for _ in range(26)
]

# (x, y)위치에서 썩기 몇 초 전인 시체의 수
dead = [
    [
        [0]*3
        for _ in range(n)
    ]

    for _ in range(n)
]

for _ in range(m):
    mx, my, mdir = map(int, input().split())
    monster[0][mx-1][my-1][mdir-1] += 1

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x,y):
    return in_range(x, y) and dead[x][y][0] == 0 and dead[x][y][1] == 0 and (x, y) != (px, py)

def get_nxt_pos(x, y, move_dir):
    for _ in range(8):
        nx, ny = x+dxs[move_dir], y+ dys[move_dir]
        if can_go(nx, ny):
            return (nx, ny, move_dir)
        move_dir = (move_dir+1)%8
    return (x, y, move_dir)

def move_monster():
    for i in range(n):
        for j in range(n):
            for k in range(8):
                x, y, n_dir = get_nxt_pos(i, j, k)
                monster[t_num][x][y][n_dir] += monster[t_num-1][i][j][k] 
                    
def get_killed_num(d1, d2, d3):
    x, y = px, py
    k_num = 0

    visited = []
    for move_dir in [d1, d2, d3]:
        nx, ny = x + p_dxs[move_dir], y + p_dys[move_dir]
        if not in_range(nx, ny): return -1
        if (nx, ny) not in visited:
            visited.append((nx, ny))
            k_num += sum(monster[t_num][nx][ny])
        x, y = nx, ny
    return k_num

def kill(best_route):
    global px, py
    
    d1, d2, d3 = best_route
    for move_dir in [d1, d2, d3]:
        nx, ny = px + p_dxs[move_dir], py + p_dys[move_dir]
        dead[nx][ny][2] += sum(monster[t_num][nx][ny])

        for i in range(8):
            monster[t_num][nx][ny][i] = 0
        px, py = nx, ny

def move_pecman():
    max_cnt = -1
    best_route = (-1, -1, -1)

    for i in range(4):
        for j in range(4):
            for k in range(4):
                m_cnt = get_killed_num(i, j, k)
                if m_cnt > max_cnt:
                    max_cnt = m_cnt
                    best_route = (i, j, k)
    kill(best_route)

def dead_monster():
    for i in range(n):
        for j in range(n):
            for k in range(2):
                dead[i][j][k] = dead[i][j][k+1]
            dead[i][j][2] = 0

def duplicate_monster():
    for i in range(n):
        for j in range(n):
            for k in range(8):
                monster[t_num][i][j][k] += monster[t_num-1][i][j][k]

def simulate():
    move_monster()
    move_pecman()

    dead_monster()
    duplicate_monster()

while t_num <= t:
    simulate()
    t_num += 1

answer = 0
for i in range(n):
    for j in range(n):
        for k in range(8):
            answer += monster[t][i][j][k]
print(answer)