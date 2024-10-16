import sys
input = sys.stdin.readline 
from collections import deque

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0
times = [[0]*M for _ in range(N)] # 가장 최근에 공격한 시간 
attacker_list = []
partitions = []

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M 

def pick_attacker():
    global attacker_list
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:continue
            attacker_list.append((arr[i][j], times[i][j], i+j, j))
    attacker_list.sort(key = lambda x:(x[0], -x[1], -x[2], -x[3]))
   
    return attacker_list[0]
    
def bfs(x, y, final_x, final_y):
    # 우/하/좌/상의 우선순위
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0] 
    visited = [[False]*M for _ in range(N)]
    #  레이저 경로에 있는 포탑도 공격을 받게 되는데,
    #  이 포탑은 공격자 공격력의 절반 만큼의 공격을 받습니다. (절반이라 함은 공격력을 2로 나눈 몫을 의미합니다.)
    que = deque()
    que.append((x, y, [(x, y)]))
    visited[x][y] = True
     
    while que:
        x, y, path = que.popleft()
        if x == final_x and y == final_y:
            return path[:]
        for dir in range(4):
            nx, ny = x + dxs[dir], y + dys[dir]
            if not in_range(nx, ny):
                nx, ny = nx%N, ny%M 
            if not visited[nx][ny] and arr[nx][ny]:
                path.append((nx, ny))
                que.append((nx, ny, path[:]))
                path.pop()
                visited[nx][ny] = True    
    return False

def potan(attack, x, y, minus):
    global arr, partitions
    p_dxs, p_dys = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]

    partitions.append((x, y))
    partitions.append(attack)
    for dir in range(8):
        nx, ny = x + p_dxs[dir], y + p_dys[dir]
        if not in_range(nx, ny):
            nx, ny = nx%N, ny%M 
        if (nx, ny) == attack:
            continue
        if not in_range(nx, ny):
            nx, ny = nx%N, ny%M 
        if arr[nx][ny]:
            arr[nx][ny] = max(0, arr[nx][ny] - minus)
            partitions.append((nx, ny))


def attack(attacker, t):
    global arr, partitions, attacker_list
    # 공격자의 위치
    x, y = attacker[2]-attacker[3], attacker[3]
    # print("attcker = ", (x, y), t)

    # 공격력 증가
    arr[x][y] += (N + M)
    times[x][y] = t

    # 가장 강한 포탑 선정 > 위치 
    strong = attacker_list[-1]
    sx, sy = strong[2]-strong[3], strong[3]
    # print("strong =", (sx, sy))

    # 레이저 공격 시도
    partitions = [(x, y)]
    path = bfs(x, y, sx, sy)
    if path != False:
        arr[sx][sy] = max(0, arr[sx][sy]- arr[x][y])
        # print("공격받은 후", arr[sx][sy])
        for px, py in path[1:-1]:
            arr[px][py] = max(0, arr[px][py] - arr[x][y]//2)
        partitions = path[:]
        # print("raser")
  
    # 포탄 공격 시도    
    else:
        arr[sx][sy] = max(0, arr[sx][sy]- arr[x][y])
        potan((x, y), sx, sy, arr[x][y]//2)
    

def plus_survivor():
    global arr
    # print("partitions ", partitions)
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                if (i, j) not in partitions:
                    arr[i][j] += 1

def simulate(t):
    global attacker_list, partitions
    # 초기화
    attacker_list = []
    partitions = [] 
    
    attacker = pick_attacker()
    attack(attacker, t)
    plus_survivor()


def game_over():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0: cnt += 1
    return cnt == 1

for t in range(1, K+1):
    if game_over():break 
    simulate(t)
    # print("time arr")
    # for row in times:
    #     print(*row)
    # print()
    # for row in arr:
    #     print(*row)
    # print()
    # print()



for i in range(N):
    for j in range(M):
        if arr[i][j]:answer = max(answer, arr[i][j])
print(answer)