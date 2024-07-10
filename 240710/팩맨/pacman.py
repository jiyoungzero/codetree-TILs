import sys
input = sys.stdin.readline 
import copy

m, t = map(int, input().split())
r, c = map(int, input().split())
pecman = [r-1, c-1]
monsters = []
dead = [] # 몬스터 시체
for _ in range(m):
    r, c, d = map(int, input().split())
    monsters.append((r-1, c-1, d-1))
arr = [[0]*4 for _ in range(4)] 


dxs, dys = [-1, -1, 0, 1, 1, 1, 0, -1], [0, -1, -1, -1, 0 ,1, 1, 1] # 위, 위-왼쪽, 왼쪽, 아래-왼쪽, 아래...
p_dxs, p_dys = [-1, 0, 1, 0], [0, -1, 0, 1] # 상, 좌, 하, 우
routes = []

def dfs(tmp, routes):
    if len(tmp) == 3:
        routes.append(tmp[:])
        return 

    for dir in range(4):
        tmp.append((p_dxs[dir], p_dys[dir]))
        dfs(tmp, routes)
        tmp.pop()   

dfs([], routes) # routes = [[(-1, 0), (-1, 0), (-1, 0)], [(-1, 0), (-1, 0), (0, -1)],...     

def can_go(nx, ny):
    if not in_range(nx, ny):return False
    if [nx, ny] == pecman: return False
    for d in dead:
        x, y, _ = d
        if (x, y) == (nx, ny):
            return False
    return True

def in_range(x, y):
    return 0 <= x < 4 and 0 <= y < 4


# 몬스터 시체가 있거나, 팩맨이 있는 경우거나 격자를 벗어나는 방향일 경우에는 반시계 방향으로 45도
# 만약 8 방향을 다 돌았는데도 불구하고, 모두 움직일 수 없었다면 해당 몬스터는 움직이지 않습니다.
def move_monsters():
    global monsters
    for idx, monster in enumerate(monsters):
        x, y, d = monster
        for _ in range(8):
            nx, ny = x + dxs[d], y + dys[d]
            if can_go(nx, ny):
                x, y = nx, ny
                break
            d = (d+1)%8
        monsters[idx] = [x, y, d]

def count_monster(paths):
    result = 0
    for path in paths:
        x, y = path
        for monster in monsters:
            mx, my, _ = monster
            if [x, y] == [mx, my]:
                result += 1
    return result

def move_pecman(time):
    global monsters, dead, pecman
    eat = [0]*64
    
    for i, route in enumerate(routes):
        x, y = pecman
        paths = set()
        flag = True
        for dx, dy in route:
            nx, ny = x + dx, y + dy
            if in_range(nx, ny):
                paths.add((nx, ny))
                x, y = nx, ny
            else: 
                flag = False
                break
        if flag:
            eat[i] = count_monster(paths)
    
    max_cnt, max_idx = eat[0], 0
    for i in range(1, 64):
        if eat[i] > max_cnt:
            max_cnt = eat[i]
            max_idx = i
    
    final_route = routes[max_idx]
    # print("현재 팩맨", pecman, " 최종 경로 ->", final_route, max_cnt, max_idx)
    x, y = pecman
    eat_idx = set()
    for dx, dy in final_route:
        x += dx
        y += dy
        for i, monster in enumerate(monsters):
            if monster[0] == x and monster[1] == y:
                dead.append([monsters[i][0], monsters[i][1], time+2])
                eat_idx.add(i)
    n_monsters = []
    for idx in range(len(monsters)):
        if idx not in eat_idx:
            n_monsters.append(monsters[idx])
    
    # 몬스터 정보 업데이트
    monsters = n_monsters

    # 팩맨 위치 업데이트
    pecman = [x, y]
    return 


def born_dup(lst):
    global monsters
    for x, y, d in lst:
        monsters.append([x, y, d])


for time in range(t):
    duplicate = copy.deepcopy(monsters)
    # print(time, "번 째 : 복제 ", duplicate)
    move_monsters() 
    # print("몬스터 이동 후 : ", monsters)
    move_pecman(time)
    # print("팩맨 이동 후 :", pecman)
    # print("팩맨 이동 후 몬스터 상태 :", monsters)
    born_dup(duplicate)
    # print("알 부화 :", duplicate, ", 최종 몬스터 : ", monsters)

    # 시체 처리
    n_dead = []
    erase = []
    for i, d in enumerate(dead):
        x, y, tt = d
        if tt == time:
            erase.append(i)
    for i in range(len(dead)):
        if i not in erase:
            n_dead.append(dead[i])
    dead = n_dead

    # print("dead :", dead)
    # print() 

print(len(monsters))